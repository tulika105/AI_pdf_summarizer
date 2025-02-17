# AI_pdf_summarizer

# 📝 Introduction
In today's fast-paced world, reading through lengthy documents can be time-consuming. The AI PDF Summarizer is designed to make this process easier by extracting key information from PDFs and generating a concise, AI-powered summary.
How does it work?
- Uploads a PDF (supports files with text only).
- Extracts only the text (ignores images without OCR).
- Uses LangChain with Mistral-8x7B via groq api.
- Incorporated CoT (Chain of thought) prompting to generate the summary.
- Allows users to choose summary **length & format**.
- Presents the summary in an easy-to-read format through the Gradio web interface.
- This project is deployed on Hugging Face Spaces, making it accessible without installation.

# 🛠️ Technologies & Frameworks Used
- Python = Main programming language
- Gradio = Web-based UI for easy interaction
- pdfplumber = Extracting text from PDFs
- LangChain	= Connecting to LLMs (Mistral-8x7B)
- Groq API = Accessing Mistral-8x7B model
- Hugging Face Spaces	= Deploying the web app online

**Get the summary here:** https://huggingface.co/spaces/Tulika2000/ai-pdf-summarizer


![Screenshot 2025-02-16 233301](https://github.com/user-attachments/assets/60d787b7-5c71-44d7-a906-0af1d65db279)
