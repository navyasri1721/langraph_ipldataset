from graph import build_graph

graph = build_graph()
chat_history = []


def ask_question(question):

    result = graph.invoke(
        {
            "user_query": question,
            "chat_history": chat_history
        }
    )

    chat_history.append(f"User: {question}")

    chat_history.append(
        f"Assistant: {result['final_answer']}"
    )

    return result["final_answer"]