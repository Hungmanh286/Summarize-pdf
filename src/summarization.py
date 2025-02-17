from transformers import pipeline

summarizer = pipeline("summarization", model="openai-community/gpt2")

def summarize_with_llm(text):
    summary = summarizer(text, max_length=512, min_length=30, do_sample=False, temperature=0.7)
    return summary[0]['summary_text']

text = "Machine learning is a method of data analysis that automates analytical model building..."
summary = summarize_with_llm(text)
print(summary)
