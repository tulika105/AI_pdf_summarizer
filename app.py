# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XblbxoRxB4XOHixjGij789FPD9KjKdhi
"""

import os
import pdfplumber
import gradio as gr
from langchain_groq.chat_models import ChatGroq

# Set Groq API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Fetch from environment variables
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Add it in Hugging Face Secrets.")

# Initialize LLM (llama-3.3-70b-versatile)
llm = ChatGroq(model_name="llama-3.3-70b-versatile")

def extract_text_from_pdf(pdf_file):
    """Extracts clean text from a text-based PDF while handling edge cases."""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text.strip() + "\n\n"  # Keep formatting clean
    except Exception as e:
        return f"Error extracting text: {str(e)}"

    if not text.strip():
        return "⚠️ No readable text found. This might be a scanned or image-based PDF."

    return text.strip()

def summarize_text(text, length, style):
    """Summarizes extracted text using Mistral-8x7B with structured formatting."""
    prompt = (
        f"""
        Read the following document and summarize it in {style.lower()} format.
        Keep the summary {length.lower()}.
        Follow this structured reasoning:
        1. Identify key sections & main topics.
        2. Extract essential points from each section.
        3. Remove redundant information.
        4. Ensure accuracy without hallucination.

        Document:
        {text[:10000]}  # Limit input to 10,000 characters for efficiency
        """
    )
    response = llm.predict(prompt)
    return response.strip()

def process_pdf(file, length, style):
    """Extracts text and summarizes PDF with customization options."""
    if not file:
        return "⚠️ No file uploaded. Please upload a PDF."

    text = extract_text_from_pdf(file.name)
    if text.startswith("⚠️") or text.startswith("Error"):
        return text  # Return error messages directly

    return summarize_text(text, length, style)

# Create Gradio Interface
interface = gr.Interface(
    fn=process_pdf,
    inputs=[
        gr.File(label="📄 Upload a PDF"),
        gr.Radio(["Short", "Medium", "Long"], label="📏 Summary Length", value="Medium"),
        gr.Radio(["Bullets", "Key Takeaways", "Concise Paragraph"], label="📌 Summary Style", value="Key Takeaways"),
    ],
    outputs="text",
    title="📄 PDF Summarizer (Text-Based PDFs Only)",
    description="Upload a PDF file (text-based only) and get a structured summary. Not for scanned/image PDFs.",
)

# Run the app
interface.launch()
