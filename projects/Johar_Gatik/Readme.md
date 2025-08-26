# Project Title: Hyper-Realistic AR Face Filter

## Student Details
- **Name**: Gatik Johar
- **PRN**: 24070126060
- **Year**: SY
- **Branch**: AIML

---

## Problem Statement
**Goal:** Create a hyper-realistic AR application that overlays virtual objects (e.g., glasses) on detected faces in real-time using a webcam. The program should be streamlined, user-friendly, and impressive.

---

## Features
- Real-time face detection using OpenCV.
- Hyper-realistic glasses overlay with dynamic lighting, 3D perspective, and lens effects.
- Support for multiple faces.
- Interactive features (e.g., toggle overlays).

---

## Tech Stack
- **Languages**: Python
- **Libraries**: OpenCV, NumPy, Pillow
- **Tools**: VS Code, Git, Virtual Environment

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/GOATIK-J/FOSS-Recruitment-2025.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FOSS-Recruitment-2025/projects/Johar_Gatik
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # For Windows
   source .venv/bin/activate  # For Linux/Mac
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the main script:
   ```bash
   python tools/ar_face_filter.py
   ```
6. Follow the on-screen instructions to test the AR functionality.

---

## Project Structure
```
project/
├── README.md
├── requirements.txt
├── tools/
│   └── ar_face_filter.py  # Final streamlined program
├── assets/
│   └── glasses.png        # Glasses overlay image
```

---

## Demo Screenshot / Output
Below is a sample output of the project:

- **Terminal Output**:
  ```
  Faces detected: 2
  Glasses overlay applied successfully.
  ```
- **Screenshot**:
  ![Demo Screenshot](assets/demo.png)

---

## Future Improvements
- Add support for additional virtual objects.
- Enhance performance for low-end devices.
- Introduce a GUI for better user interaction.

---

## Notes for Reviewers
- Ensure the `requirements.txt` dependencies are installed before running the project.
- The program has been tested on Windows and Linux.

---

## Submission Checklist
- [x] Cloned the Repository
- [x] Added my details (Name, PRN, Year, Branch)
- [x] Wrote Problem Statement
- [x] Listed Features & Tech Stack
- [x] Added clear Run Instructions
- [x] Provided Demo Output (screenshot or text)
- [x] Explained Future Improvements
- [x] Project runs offline

