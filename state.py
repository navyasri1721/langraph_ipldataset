from typing import TypedDict, List

class IPLState(TypedDict, total=False):

    user_query: str
    query_type: str

    chat_history: List[str]

    team_context: str
    batting_context: str
    bowling_context: str
    h2h_context: str
    venue_context: str
    form_context: str
    trend_context: str
    records_context: str

    final_answer: str