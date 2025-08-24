# Project Title: Console-Based Pixel Art Generator

## Student Details
- **Name**: Ratnesh kumar  
- **PRN**: 24070123083
- **Year**: SY 
- **Branch**: ENTC 

---

## Problem Statement
This project enables beginners to create colorful pixel art in the terminal using simple text inputs, transforming basic characters into vibrant ASCII designs for a fun, retro-inspired creative experience.

---

## Features
- Create colorful pixel art in the terminal from simple text inputs (e.g., 'r' for red, 'b' for blue).
- Display predefined patterns like a heart for instant testing.
- Works fully offline with no external dependencies.

---

## Tech Stack
- Python
- ANSI escape codes (for terminal color output)
- Built-in Python modules: `sys`, `time`

---

## How to Run
1. Ensure Python 3.8+ is installed on your system.
2. Open a terminal and navigate to the project source folder: `cd projects/lastname_firstname/src`.
3. Run the script with `python pixel_art.py`.
4. Follow the on-screen prompts: Enter the grid size (e.g., 5), then input each row's characters, or type 'sample' for a predefined pattern.
5. View the colored pixel art output in the terminal; enter 0 for grid size to exit.

---

## Project Structure

projects/kumar_ratnesh/

├── README.md              
├── requirements.txt       
├── src/<br>
│   └── pixel_art.py      
└── sample_output.txt          
---

## Demo Screenshot / Output
Console Pixel Art Generator<br>
Use: r=red, b=blue, g=green, y=yellow, w=white, .=empty<br>
Enter 'sample' for a predefined heart pattern.<br>
Enter grid size (e.g., 5 for 5x5, 0 to exit): 3<br>
Enter 3 rows of 3 chars (r,b,g,y,w,.)<br>
Row 1: .r.<br>
Row 2: rrr<br>
Row 3: .r.<br>

<img width="174" height="128" alt="image" src="https://github.com/user-attachments/assets/4c81b167-238a-4af6-89fd-da28ef86580e" />
    
---

## AI Tools Used
GitHub Copilot, Grok

---

## Future Improvements
If I had more time to make the **Console-Based Pixel Art Generator** better, I’d add:

1. **Save Art**: Save your designs to a file to use later.
2. **More Colors**: Add fun colors like pink or purple.
3. **Easy Editor**: Use arrow keys to draw pixels in the terminal.
4. **Moving Art**: Show patterns that move like a mini cartoon.
5. **Save as Picture**: Turn your art into a PNG image.
6. **More Examples**: Add cool shapes like stars or trees.
7. **Better Help**: Nicer error messages to fix mistakes easily.


---

## Notes for Reviewers
This project runs fully offline with no external dependencies, using only Python’s built-in `sys` and `time` modules. For best results, run in a terminal supporting ANSI colors (e.g., Windows Terminal, Git Bash, or Linux/macOS terminals).

---

## Submission Checklist 
- [x] Cloned the Repository 
- [x] Added my details (Name, PRN, Year, Branch)  
- [x] Wrote Problem Statement  
- [x] Listed Features & Tech Stack  
- [x] Added clear Run Instructions  
- [x] Provided Demo Output (screenshot or text)  
- [x] Listed AI tools used (or None)  
- [x] Explained Future Improvements  
- [x] Project runs offline

