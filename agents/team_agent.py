from utils.retriever import retriever

def team_node(state):

    query = state["user_query"]

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return {
        "team_context": context
    }