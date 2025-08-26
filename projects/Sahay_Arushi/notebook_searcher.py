import os
import cv2
import pytesseract
from PyPDF2 import PdfReader
import fitz # PyMuPDF

# This line is needed if tesseract is not in your system's PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts text from an image using OCR.
    """
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

def extract_text_from_files(folder_path):
    """
    Extracts text content from .txt, .pdf, and image files.
    Handles both searchable and scanned-image PDFs.
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
                content = ""
                # First, try to extract text from a searchable PDF
                with open(file_path, "rb") as f:
                    reader = PdfReader(f)
                    for page in reader.pages:
                        content += page.extract_text() or ""

                # If no text was extracted, assume it's an image-based PDF
                if not content.strip():
                    doc = fitz.open(file_path)
                    for page_num, page in enumerate(doc):
                        # Render the page as an image
                        pix = page.get_pixmap()
                        img_path = os.path.join(folder_path, f"temp_page_{page_num}.png")
                        pix.save(img_path)
                        # Run OCR on the image
                        content += pytesseract.image_to_string(img_path)
                        os.remove(img_path) # Clean up temp image file
                
                text_data[filename] = content
            except Exception as e:
                print(f"Error processing PDF {filename}: {e}")
        
        elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            content = extract_text_from_image(file_path)
            text_data[filename] = content

    return text_data

def search_notes(notes_dict, keyword):
    """
    Searches for a keyword in the text content of the notes.
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
                # Use 'q' as the exit command
                search_query = input("\nEnter a keyword to search (or type 'q' to quit): ")
                if search_query.lower() == 'q':
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