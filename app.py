# app.py
import gradio as gr
from google.generativeai import genai
import os

# Set your API key
genai.configure(api_key=os.getenv("AIzaSyCqpDOzqCE_y56WQTCvR5gU7tHQe40pUvk"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat function
def chat_with_gemini(user_msg):
    if not user_msg:
        return "Please type a message."
    try:
        response = model.generate_content(user_msg)
        return response.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=chat_with_gemini,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Gemini AI Chatbot",
    description="Chat with Gemini AI using HuggingFace Spaces"
)

# Launch the app
iface.launch()
