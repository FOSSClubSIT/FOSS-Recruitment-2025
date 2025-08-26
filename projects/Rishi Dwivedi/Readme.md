# Project Title: FOSS Learning Website

## Student Details
- **Name**: Rishi 
- **PRN**: 24070126152 
- **Year**: SY 
- **Branch**: AIML  

---

## Problem Statement
Learning a new technical skill is often confusing due to the overwhelming number of resources available. This project solves that problem by providing clean, curated, and interactive learning roadmaps for various technologies, guiding students from one step to the next.

---

## Features
Some of the things my Project can do are
- **Dynamic Roadmaps:** Displays curated, step-by-step learning paths for various skills (Python, JavaScript, etc.).
- **Interactive Course Pages:** Each roadmap step links to a detailed page with notes, practical tasks, and an interactive quiz.
- **Progress Tracking:** The application uses `localStorage` to remember which modules a user has "visited" or "completed" by passing a quiz, providing a persistent sense of accomplishment.
- **Modern UI/UX:** A clean, developer-focused dark theme with smooth animations and a responsive layout for a great user experience.
- **Community Feedback:** A floating action button allows users to request new roadmaps via a simple form, ensuring the platform grows based on community needs.

---

## Tech Stack
Tools Used
- **HTML5**
- **CSS3** (including CSS Variables, Flexbox, and Grid)
- **Vanilla JavaScript (ES6+)** (AI Help needed)
- **Gemini**
- **Claude**

---

## How to Run
## Method 1: The Easiest Way (No Tools Needed)
This method works by opening the file directly in your browser.
1.Get the Files: Make sure you have the project folder on your computer, either by downloading it as a ZIP or using git clone.
2.Open the Folder: Use your computer's File Explorer (or Finder on a Mac) to navigate into the project folder.
3.Double-Click index.html: Find the index.html file and simply double-click it.
    This will open your website in your default web browser using a file:/// path.
## Method 2: The Better Way (Using VS Code Live Server)
1.This method uses a free VS Code extension to create a simple local server, which is a better practice for web development.
2.Open in VS Code: Open your entire project folder in Visual Studio Code.
3.Install Live Server: Go to the Extensions tab (Ctrl+Shift+X), search for "Live Server", and click Install.
4.Go Live: Once installed, right-click on your index.html file in the VS Code explorer and choose "Open with Live Server".
    Your website will automatically open in a new browser tab with a local server address like http://127.0.0.1:5500. The best part is that the page will auto-reload every time you save a change to your code.



---

## Project Structure

FOSS-Recruitment-2025\projects\Rishi Dwivedi
├── README.md
├── index.html       # The main home page
├── roadmap.html     # Page for displaying a skill's roadmap
├── course.html      # Page for a specific course module

---

## Demo Screenshot / Output
![Screenshot 1](./ScreenShot/Screenshot%202025-08-26%20230551.png)
![Screenshot 2](./ScreenShot/Screenshot%202025-08-26%20230613.png)
![Screenshot 3](./ScreenShot/Screenshot%202025-08-26%20230640.png)
![Screenshot 4](./ScreenShot/Screenshot%202025-08-26%20230651.png)
![Screenshot 5](./ScreenShot/Screenshot%202025-08-26%20230710.png)
---

## AI Tools Used
Gemini(For Speeding up the programming Procedure)
Anthropic's Claude(For improving code quality)

---

## Future Improvements
Possible Improvements if Given More Time-
->Backend API with Admin Panel: Instead of hardcoding roadmaps, I would build a backend (Node.js + Express) with an admin dashboard. Verified users could log in and directly create or edit courses using premade templates. This would make it easy to add new topics or update existing roadmaps without touching the codebase.
->Git-based CMS Integration: Roadmaps could also be managed in Markdown files on GitHub, where contributors submit Pull Requests. This hybrid approach (admin panel + GitHub contributions) would balance ease of use with community-driven collaboration.
->User Accounts & Progress Tracking: A simple authentication system would allow users to save progress, sync it across devices, and even see community stats (like how many people completed a roadmap).
->Gamification Elements: Features such as badges, streaks, and leaderboard challenges could make the platform more engaging and help maintain learner motivation.
->Make the homepage hero more engaging with better visuals and a clear call-to-action.
->Refine the roadmap cards so that each course path feels a bit more unique and appealing.
->On the roadmap pages, I’d like to add progress indicators so learners can see how far they’ve come.

Also This page isnt fully optimized for other screen sizes like Mobile,Tv etc

---

## Notes for Reviewers
- This project is a completely static, frontend-only application. All data is currently hardcoded within the JavaScript of each page.
- All user progress is saved locally in the browser's `localStorage`. Clearing browser data will reset progress.
- The project is designed to be self-contained and run without an internet connection (once the Google Fonts are cached).
    (Though Some feautures like image aren't locally stored so will require Internet)

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

