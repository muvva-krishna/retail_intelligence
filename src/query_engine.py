
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.experimental.query_engine import PandasQueryEngine


def build_rag_engine(index, top_k):
    retriever = index.as_retriever(similarity_top_k=top_k)
    return RetrieverQueryEngine.from_args(retriever)


def build_pandas_engine(df):
    return PandasQueryEngine(df=df, verbose=False)


def route_query(question: str):
    numeric_keywords = ["total", "sum", "average", "mean", "highest", "lowest"]

    if any(word in question.lower() for word in numeric_keywords):
        return "pandas"
    return "rag"
