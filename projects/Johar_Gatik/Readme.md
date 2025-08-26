# Project Title: Mini AR with OpenCV 

## Student Details
- **Name**: Gatik Johar  
- **PRN**: 24070126060  
- **Year**: SY  
- **Branch**: AIML 

---

## Problem Statement
**Goal:** Detect a known flat reference image inside a scene (or webcam) using feature matching and RANSAC homography, then draw a 3D cube aligned to the detected plane — fully offline by default.

---

## Features
- ORB feature detection & Hamming BF matching.
- RANSAC-based homography estimation.
- Quadrilateral overlay of detected reference plane.
- Optional virtual 3D cube overlay via homography → pose decomposition.
- Offline sample generator (`tools/generate_samples.py`).
---

## Tech Stack
- **Languages**: Python  
- **Libraries**: OpenCV, NumPy, Matplotlib  
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
   python src/ar_demo.py
   ```
6. Follow the on-screen instructions to test the AR functionality.

---

## Project Structure
```
your-project/
├── README.md
├── requirements.txt
├── src/            # Source code
│   ├── ar_demo.py  # Main script
│   ├── features.py # Feature detection and matching
│   ├── io_utils.py # Input/output utilities
│   ├── overlay.py  # Overlay rendering
│   ├── pose.py     # Pose estimation
├── tools/          # Utility scripts
│   └── generate_samples.py # Offline sample generator
└── sample_output/  # (optional) Generated outputs
```

---

## Demo Screenshot / Output
Below is a sample output of the project:

- **Terminal Output**:
  ```
  Reference image detected.
  Homography matrix computed.
  3D cube overlay rendered successfully.
  ```
- **Screenshot**:
  ![Demo Screenshot](docs/demo_screenshot.png)  

---

## AI Tools Used
- GitHub Copilot

---

## Future Improvements
- Add support for multiple reference images.
- Improve the accuracy of feature matching.
- Optimize the performance for real-time AR applications.
- Add a GUI for better user interaction.

---

## Notes for Reviewers
- This project runs offline by default.
- Ensure the `requirements.txt` dependencies are installed before running the project.

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

