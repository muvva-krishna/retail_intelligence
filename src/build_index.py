# ==========================================
# RAG Index Builder (SimpleVectorStore)
# ==========================================

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.vector_stores.simple import SimpleVectorStore

from config import MAX_ROWS_FOR_INDEX


def create_documents(df):
    documents = []

    for _, row in df.head(MAX_ROWS_FOR_INDEX).iterrows():

        text = (
            f"Invoice {row['InvoiceNo']} from {row['Country']} on "
            f"{row['InvoiceDate'].date()}.\n"
            f"Product: {row['Description']}.\n"
            f"Quantity: {row['Quantity']}.\n"
            f"Unit Price: {row['UnitPrice']}.\n"
            f"Revenue: {row['Revenue']}.\n"
            f"Customer ID: {row['CustomerID']}."
        )

        metadata = {
            "country": row["Country"],
            "month": row["YearMonth"],
            "revenue": float(row["Revenue"]),
            "customer_id": row["CustomerID"]
        }

        documents.append(Document(text=text, metadata=metadata))

    return documents


def build_vector_index(documents):

    # Simple in-memory vector store
    vector_store = SimpleVectorStore()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    return index
