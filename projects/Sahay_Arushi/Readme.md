# Project Title:  Offline Notebook Searcher

## Student Details
- **Name**: Arushi Sahay  
- **PRN**: 25070126035  
- **Year**: FY  
- **Branch**: AIML  

---

## Problem Statement
Students often have notes scattered across multiple text files, PDFs, and even images. It's time-consuming to find a specific piece of information, like a single formula or definition, during revision. This project solves that problem by creating a centralized, searchable database of a student's notes.

---

## Features
Local Indexing: Scans and reads notes from a designated local folder.

Keyword Search: Allows users to search for specific keywords or phrases.

Contextual Results: Displays search results with the filename, line number, and a snippet of the matching text.

Case-Insensitive Search: Matches keywords regardless of capitalization.

Offline-First: The entire tool runs without an internet connection.


---

## Tech Stack
Languages: Python

Libraries: os, re (for basic search). The following libraries are planned for future improvements: PyPDF2 (for PDF support), pytesseract and OpenCV (for OCR functionality).
---

## How to Run
Explain step by step how to run your project.  
Example:  
1. Open the folder in VS Code.  
2. Run `python main.py`  
3. The program will start in offline mode.

---

## Project Structure

your-project/ ├── README.md ├── src/        # your code ├── docs/       # (optional) documentation └── sample_output/   # (optional) if you use APIs

---

## Demo Screenshot / Output
Add a screenshot of your project running, or copy-paste sample terminal output here.

---

## AI Tools Used
I used ChatGPT and Gemini for this project. It helped with:

Code Snippets and Logic: I brainstormed a few ideas myself, tried to incorporate a few logic flows from what I had understood in my previous attempt and confirmed if it was the right thinking. I asked for small code snippets to learn from and incorporated them into my own code.

Debugging: It assisted with understanding errors and finding solutions.



---

## Future Improvements
PDF Support: Integrate a library like PyPDF2 to allow searching within PDF documents.

Image OCR: Add a feature to convert images of notes to text using pytesseract and OpenCV, making handwritten or scanned notes searchable.

Regex Search: Allow users to perform more powerful searches using regular expressions.

GUI: Develop a simple graphical user interface to make the tool more user-friendly.


---

## Notes for Reviewers
This project is designed to be fully offline, respecting the FOSS recruitment guidelines. It does not require any internet connection to run after the initial setup.

---

## Submission Checklist 
- [x] Cloned the Repository 
- [x] Added my details (Name, PRN, Year, Branch)  
- [x] Wrote Problem Statement  
- [ ] Listed Features & Tech Stack  
- [ ] Added clear Run Instructions  
- [ ] Provided Demo Output (screenshot or text)  
- [ ] Listed AI tools used (or None)  
- [ ] Explained Future Improvements  
- [ ] Project runs offline

