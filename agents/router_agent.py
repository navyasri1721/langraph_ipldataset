def router_node(state):

    query = state["user_query"].lower()

    # Team Queries
    if any(word in query for word in [
        "captain",
        "coach",
        "titles",
        "team",
        "home ground"
    ]):
        qtype = "team"

    # Trend Queries
    elif any(word in query for word in [
        "season",
        "2019",
        "2020",
        "2021",
        "2022",
        "2023",
        "2024",
        "trend",
        "consistent",
        "more than once"
    ]):
        qtype = "trend"

    # Form Queries
    elif any(word in query for word in [
        "form",
        "last 5",
        "recent"
    ]):
        qtype = "form"

    # Venue Queries
    elif any(word in query for word in [
        "pitch",
        "stadium",
        "venue",
        "ground",
        "wankhede",
        "chinnaswamy",
        "eden gardens"
    ]):
        qtype = "venue"

    # Head-to-Head Queries
    elif "vs" in query:
        qtype = "h2h"

    # Bowling Queries
    elif any(word in query for word in [
        "wicket",
        "wickets",
        "economy",
        "bowling",
        "bumrah",
        "rashid",
        "chahal"
    ]):
        qtype = "bowling"

    # Batting Queries
    elif any(word in query for word in [
        "runs",
        "batting",
        "strike rate",
        "century",
        "fifty",
        "average",
        "kohli",
        "rohit",
        "rahul"
    ]):
        qtype = "batting"

    # Comparison Queries
    elif "compare" in query:
        qtype = "records"

    else:
        qtype = "records"

    print(f"\nROUTER → {qtype}")

    return {
        "query_type": qtype
    }