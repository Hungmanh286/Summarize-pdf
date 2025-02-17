from .retrieval import retrieve_chunks
from .summarization import summarize_with_llm

def chat_with_pdf(query, index, chunks):
    relevant_chunks = retrieve_chunks(query, index, chunks)
    context = " ".join(relevant_chunks)
    summary = summarize_with_llm(context)
    return summary