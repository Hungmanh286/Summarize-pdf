import os
from src.pdf_processing import extract_text_from_pdf, chunk_text
from src.embeddings import generate_embeddings, build_faiss_index, save_faiss_index
from src.chat_interface import chat_with_pdf


pdf_folder = "data/pdfs/"
index_path = "data/faiss_index/pdf_index.faiss"


pdf_path = os.path.join(pdf_folder, "example.pdf")
text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(text)


embeddings = generate_embeddings(chunks)
index = build_faiss_index(embeddings)
save_faiss_index(index, index_path)


query = "What is the main topic of the PDF?"
summary = chat_with_pdf(query, index, chunks)
print("Summary:", summary)