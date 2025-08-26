import gradio as gr
import time
import os
from datetime import datetime
from google import genai
from google.genai import types

GEMINI_API_KEY = "AIzaSyCI5wrC-DPyxKXEfIhw40S-7kY6tXyqdD8"  #hardcoding the api key (last minute)

if not GEMINI_API_KEY:
    raise ValueError("Missing Gemini API Key! Please paste it in GEMINI_API_KEY.")

client = genai.Client(api_key=GEMINI_API_KEY)

#OCR WITH GEMINI 
def extract_recipe(image_path):
    with open(image_path, "rb") as f:
        img_bytes = f.read()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # try gemini-1.5-pro if handwriting is messy
            contents=[
                types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                "Extract this recipe clearly. Format with 'Ingredients:' and 'Instructions:'."
            ]
        )
        return response.text
    except Exception as e:
        return f"Gemini OCR Error: {e}"
    
#SAVE TO FILE 
SAVE_DIR = "recipes"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_recipe(text):
    if not text.strip():
        return "No recipe to save."
    filename = f"recipe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return f"✅ Recipe saved as {filename} in '{SAVE_DIR}' folder."

