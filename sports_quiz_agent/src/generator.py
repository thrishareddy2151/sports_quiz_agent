from google import genai


from src.config import GEMINI_API_KEY
from src.database import query_historic_facts
from src.search import get_live_news_context


def compile_quiz_data(sport, difficulty):
    """
    1. Gathers context from ChromaDB (Historical).
    2. Gathers context from DuckDuckGo (Live news).
    3. Blends them inside a grounded prompt.
    4. Connects to Gemini and generates the structured quiz.
    """

    # Retrieve historical context
    db_query = (
    f"Important historical facts about {sport}, famous players, "
    f"records, tournaments, championships, rules and achievements."
    )
    db_matches = query_historic_facts(
        sport=sport,
        query_text=db_query,
        n_results=10
    )

    db_context = (
        "\n".join(db_matches)
        if db_matches
        else "No offline historic data recorded."
    )

    # Retrieve live web context
    web_context = get_live_news_context(sport)

    # Combine contexts
    unified_context = f"""
=== HISTORICAL FACTS ===
{db_context}

=== LIVE INTERNET NEWS ===
{web_context}
"""

    # System Prompt
    system_instruction = f"""
You are an expert sports quiz creator.

Use ONLY the information provided below.

The context contains TWO sources:

1. Historical facts from the local ChromaDB.
2. Recent sports news from the live web.

IMPORTANT:

- You MUST use only the information present in the provided context.
- Never invent facts or use outside knowledge.
- Every question must be based on a DIFFERENT fact.
- Avoid asking multiple questions about the same event or tournament.
- If recent web information contains verified completed events or achievements, create ONE question from it.
- Ignore future schedules, predictions, advertisements, or incomplete news snippets.
- If the web context is not useful, generate all questions from historical facts.
- Questions should be engaging, suitable for social media quizzes, and factually accurate.

Context:

{unified_context}
"""

    # Difficulty-specific instructions
    difficulty_instruction = {
    "Easy": (
        "Generate beginner-friendly questions. "
        "Focus on famous players, popular tournaments, basic rules, and well-known historical events. "
        "Avoid years, statistics, obscure records, or difficult comparisons."
    ),
    "Medium": (
        "Generate moderately challenging questions. "
        "Mix historical events, tournament winners, player achievements, important records, and famous matches. "
        "Some questions may include years or notable statistics."
    ),
    "Hard": (
        "Generate advanced questions for sports enthusiasts. "
        "Include historical records, exact years, statistics, rule-based scenarios, lesser-known achievements, and comparisons between players or tournaments."
    )
    }.get(difficulty, "Ask questions appropriate for the selected difficulty.")

    # User Prompt
    user_prompt = f"""
Generate exactly 5 multiple-choice questions.

Sport: {sport}

Difficulty: {difficulty}

Difficulty Guidance:
{difficulty_instruction}

Rules:

1. Generate EXACTLY 5 unique multiple-choice questions.
2. Every question must test a DIFFERENT fact.
3. Never ask two questions about the same event, match, tournament, or record.
4. Cover as many different categories as possible.
5. Use this distribution whenever possible:
   - 1 History
   - 1 Famous Player
   - 1 Tournament or Championship
   - 1 Record or Achievement
   - 1 Recent News (only if reliable)
6. Follow the selected difficulty strictly.
7. Use clear and natural English.
8. Each question must have exactly four options (A, B, C, D).
9. Only one option should be correct.
10. Make incorrect options believable but clearly incorrect.
11. Explanations should be short (1–2 sentences) and directly supported by the retrieved context.
12. If the retrieved context does not contain enough information for a category, choose another fact instead of inventing information.
13. IMPORTANT:
   - The Correct Answer line MUST contain ONLY the option letter.
   - Valid values are ONLY: A, B, C, or D.
   - DO NOT include the option text.
   - DO NOT write "A) Sachin Tendulkar".
   - Write ONLY:
     Correct Answer: A

Possible topics:
- History
- Famous Players
- Records
- Rules
- Major Tournaments
- Stadiums
- International Competitions
- Recent Achievements

Output Format:

Sport: <Sport Name>

f"Difficulty target: {difficulty}.\n\n"
        "Format each question exactly as follows so my program can parse it:\n"
        "Question: [Question text here]\n"

        "A) [Option A]\n"
        "B) [Option B]\n"
        "C) [Option C]\n"
        "D) [Option D]\n"

        "Correct Answer: [Only Single Option, e.g., A]\n"
        
        "Explanation: [Detailed background reasoning quoting from the context details]\n"
"""

    print("\n========== CHROMADB ==========")
    print(db_context)

    print("\n========== WEB ==========")
    print(web_context)

    print("API Key:", GEMINI_API_KEY[:15] + "...")
    
    # Create Gemini client
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Generate response
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"{system_instruction}\n\n{user_prompt}",
    )

    return response.text, unified_context