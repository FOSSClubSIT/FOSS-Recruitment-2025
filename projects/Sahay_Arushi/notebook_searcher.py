import os
import cv2  # OpenCV for image processing
import pytesseract
from PyPDF2 import PdfReader

# This line is needed if tesseract is not in your system's PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts text from an image using OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(gray)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

def extract_text_from_files(folder_path):
    """
    Extracts text content from .txt, .pdf, and image files in a given folder.

    Args:
        folder_path (str): The path to the folder containing the notes.

    Returns:
        dict: A dictionary where keys are filenames and values are their text content.
    """
    text_data = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                text_data[filename] = content
        
        elif filename.endswith(".pdf"):
            try:
                with open(file_path, "rb") as f:
                    reader = PdfReader(f)
                    content = ""
                    for page in reader.pages:
                        content += page.extract_text() or ""
                    text_data[filename] = content
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        
        # New code for images
        elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            content = extract_text_from_image(file_path)
            text_data[filename] = content

    return text_data

def search_notes(notes_dict, keyword):
    """
    Searches for a keyword in the text content of the notes.

    Args:
        notes_dict (dict): A dictionary of notes (filename: content).
        keyword (str): The keyword to search for.

    Returns:
        dict: A dictionary of search results (filename: list of matching lines).
    """
    results = {}
    for filename, content in notes_dict.items():
        matching_lines = []
        lines = content.splitlines()
        
        for line_number, line in enumerate(lines, start=1):
            if keyword.lower() in line.lower():
                matching_lines.append(f"Line {line_number}: {line.strip()}")
        
        if matching_lines:
            results[filename] = matching_lines
    return results

if __name__ == "__main__":
    notes_folder = "sample_notes"
    
    if not os.path.exists(notes_folder):
        print(f"Error: The folder '{notes_folder}' does not exist.")
    else:
        notes_data = extract_text_from_files(notes_folder)

        if not notes_data:
            print("No searchable files found in the notes folder. Please add some notes to search.")
        else:
            while True:
                search_query = input("\nEnter a keyword to search (or type 'exit' to quit): ")
                if search_query.lower() == 'exit':
                    break

                search_results = search_notes(notes_data, search_query)

                if search_results:
                    print("\n--- Search Results ---")
                    for filename, matches in search_results.items():
                        print(f"\nFound in {filename}:")
                        for match in matches:
                            print(f"  - {match}")
                    print("--------------------")
                else:
                    print(f"No results found for '{search_query}'.")