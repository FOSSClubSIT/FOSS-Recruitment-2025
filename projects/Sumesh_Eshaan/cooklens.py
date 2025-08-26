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
os.makedirs(SAVE_DIR, exist_ok=True) #makes directory in cd

def save_recipe(text):
    if not text.strip():
        return "No recipe to save."
    filename = f"recipe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return f"✅ Recipe saved as {filename} in '{SAVE_DIR}' folder."

#TIMER FUNCTIONS
timer_start = None
timer_duration = None

def start_timer(seconds):
    global timer_start, timer_duration
    try:
        timer_duration = int(seconds)
        timer_start = time.time()
        return f"⏱️ Timer started for {seconds} seconds."
    except:
        return "Enter a valid number."

def get_timer():
    global timer_start, timer_duration
    if timer_start is None:
        return "No timer running."
    elapsed = int(time.time() - timer_start)
    remaining = timer_duration - elapsed
    if remaining <= 0:
        timer_start = None
        return "⏰ Time's up!"
    return f"{remaining} seconds remaining"

#UNIT CONVERTER
conversion_table = {
    ("grams", "cups"): 0.0042,
    ("cups", "grams"): 240,
    ("ml", "cups"): 0.0042,
    ("cups", "ml"): 240,
    ("tbsp", "tsp"): 3,
    ("tsp", "tbsp"): 1/3,
}

def convert_units(amount, from_unit, to_unit):
    try:
        amount = float(amount)
        factor = conversion_table.get((from_unit, to_unit))
        if factor:
            return f"{amount * factor:.2f} {to_unit}"
        else:
            return "Conversion not available."
    except:
        return "Invalid input."
    
# GRADIO UI
with gr.Blocks() as demo:
    gr.Markdown("# 🍳 Kitchen Helper App")

    # Tab 1: OCR
    with gr.Tab("📷 Recipe OCR"):
        img_in = gr.Image(type="filepath", label="Upload recipe image")
        recipe_text = gr.Textbox(label="Extracted Recipe", lines=10)
        extract_btn = gr.Button("Extract Text with Gemini")
        save_btn = gr.Button("Save Recipe")
        save_status = gr.Textbox(label="Save Status", interactive=False)

        extract_btn.click(extract_recipe, inputs=img_in, outputs=recipe_text)
        save_btn.click(save_recipe, inputs=recipe_text, outputs=save_status)

    # Tab 2: Timer
    with gr.Tab("⏱️ Timer"):
        timer_input = gr.Textbox(label="Seconds")
        start_btn = gr.Button("Start Timer")
        timer_status = gr.Textbox(label="Status", interactive=False)
        timer_display = gr.Textbox(label="Current Time", interactive=False)

        start_btn.click(start_timer, inputs=timer_input, outputs=timer_status)
        timer = gr.Timer(value=1)
        timer.tick(fn=get_timer, outputs=timer_display)

    # Tab 3: Converter
    with gr.Tab("⚖️ Measurement Converter"):
        amount = gr.Textbox(label="Amount")
        from_unit = gr.Dropdown(["grams", "cups", "ml", "tbsp", "tsp"], label="From")
        to_unit = gr.Dropdown(["grams", "cups", "ml", "tbsp", "tsp"], label="To")
        result = gr.Textbox(label="Converted Value")
        convert_btn = gr.Button("Convert")
        convert_btn.click(convert_units, inputs=[amount, from_unit, to_unit], outputs=result)

demo.launch()