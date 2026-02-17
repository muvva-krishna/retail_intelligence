# ==========================================
# Main Orchestration Script
# ==========================================

from config import DATA_PATH, TOP_K_RETRIEVAL
from preprocess import load_and_clean_data, compute_kpis
from build_index import create_documents, build_vector_index
from query_engine import build_rag_engine, build_pandas_engine, route_query
from evaluate import evaluate_numeric
from llm_setup import initialize_gemini


def main():

    print("Initializing Gemini...")
    initialize_gemini()

    print("Loading and preprocessing data...")
    df = load_and_clean_data(DATA_PATH)

    print("Computing KPIs...")
    kpis = compute_kpis(df)

    print("Building documents and index...")
    documents = create_documents(df)
    index = build_vector_index(documents)

    print("Setting up query engines...")
    rag_engine = build_rag_engine(index, TOP_K_RETRIEVAL)
    pandas_engine = build_pandas_engine(df)

    print("\nSystem Ready.\n")

    while True:
        question = input("Ask a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        route = route_query(question)

        if route == "pandas":
            response = pandas_engine.query(question)
        else:
            response = rag_engine.query(question)

        print("\nAnswer:\n", response)

        # Example numeric evaluation
        if "total revenue" in question.lower():
            result = evaluate_numeric(response, kpis["total_revenue"])
            print("\nEvaluation:", result)


if __name__ == "__main__":
    main()
