def validation_node(state):

    query = state["user_query"].lower()

    # Out-of-scope questions
    out_of_scope_keywords = [
        "bcci",
        "world cup",
        "football",
        "nba",
        "ipl 2027",
        "ipl 2028"
    ]

    if any(keyword in query for keyword in out_of_scope_keywords):
        return {
            "final_answer":
            "This question is outside the IPL dataset scope."
        }

    # Vague questions
    vague_queries = [
        "cricket",
        "tell me everything about cricket",
        "tell me about cricket",
        "everything about cricket"
    ]

    if query.strip() in vague_queries:
        return {
            "final_answer":
            "Please ask a specific IPL-related question."
        }

    # Valid query
    return {}