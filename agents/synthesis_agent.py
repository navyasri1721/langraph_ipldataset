from utils.llm import get_llm

llm = get_llm()

def synthesis_node(state):

    context = f"""

    Team:
    {state.get('team_context','')}

    Batting:
    {state.get('batting_context','')}

    Bowling:
    {state.get('bowling_context','')}

    H2H:
    {state.get('h2h_context','')}

    Venue:
    {state.get('venue_context','')}

    Form:
    {state.get('form_context','')}

    Trend:
    {state.get('trend_context','')}

    Records:
    {state.get('records_context','')}
    """

    # Check whether any agent actually returned context
    all_context = (
        state.get("team_context", "") +
        state.get("batting_context", "") +
        state.get("bowling_context", "") +
        state.get("h2h_context", "") +
        state.get("venue_context", "") +
        state.get("form_context", "") +
        state.get("trend_context", "") +
        state.get("records_context", "")
    )

    if not all_context.strip():
        return {
            "final_answer":
            "The requested information is not available in the dataset."
        }

    prompt = f"""
You are an IPL analytics expert.

Use ONLY the provided context.

If the answer is not present in the context, say:
"The requested information is not available in the dataset."

Context:
{context}

Question:
{state["user_query"]}

Provide a clear and concise answer.
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }