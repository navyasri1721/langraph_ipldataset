from langgraph.graph import StateGraph, END

from state import IPLState

from agents.router_agent import router_node
from agents.validation_agent import validation_node

from agents.batting_agent import batting_node
from agents.bowling_agent import bowling_node
from agents.venue_agent import venue_node
from agents.h2h_agent import h2h_node
from agents.form_agent import form_node
from agents.records_agent import records_node
from agents.team_agent import team_node
from agents.trend_agent import trend_node

from agents.synthesis_agent import synthesis_node


def validation_route(state):

    if state.get("final_answer"):
        return "end"

    return state["query_type"]


def build_graph():

    graph = StateGraph(IPLState)

    # Nodes
    graph.add_node("router", router_node)

    graph.add_node("validation", validation_node)

    graph.add_node("batting", batting_node)
    graph.add_node("bowling", bowling_node)
    graph.add_node("venue", venue_node)
    graph.add_node("h2h", h2h_node)
    graph.add_node("form", form_node)
    graph.add_node("records", records_node)
    graph.add_node("team", team_node)
    graph.add_node("trend", trend_node)

    graph.add_node("synthesis", synthesis_node)

    # Entry Point
    graph.set_entry_point("router")

    # Router → Validation
    graph.add_edge("router", "validation")

    # Validation → Agent
    graph.add_conditional_edges(
        "validation",
        validation_route,
        {
            "batting": "batting",
            "bowling": "bowling",
            "venue": "venue",
            "h2h": "h2h",
            "form": "form",
            "records": "records",
            "team": "team",
            "trend": "trend",
            "end": END
        }
    )

    # Agent → Synthesis
    graph.add_edge("batting", "synthesis")
    graph.add_edge("bowling", "synthesis")
    graph.add_edge("venue", "synthesis")
    graph.add_edge("h2h", "synthesis")
    graph.add_edge("form", "synthesis")
    graph.add_edge("records", "synthesis")
    graph.add_edge("team", "synthesis")
    graph.add_edge("trend", "synthesis")

    # Synthesis → END
    graph.add_edge("synthesis", END)

    return graph.compile()