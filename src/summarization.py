import google.generativeai as genai

# Khởi tạo API key (Thay thế bằng API key của bạn)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def summarize_with_llm(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize the following text in 3-5 sentences: {text}")
    return response.text  # Trả về nội dung tóm tắt

# Ví dụ sử dụng
text = "Machine learning is a method of data analysis that automates analytical model building..."
summary = summarize_with_llm(text)
print(summary)
