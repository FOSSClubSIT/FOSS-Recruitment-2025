# Pull Request Description

## Summary
This pull request introduces the final version of the Hyper-Realistic AR Face Filter project. The program overlays virtual glasses on detected faces in real-time using OpenCV, ensuring hyper-realistic effects with dynamic lighting, 3D perspective, and lens effects.

## Changes Made
- Integrated all functionality into `ar_face_filter.py`.
- Refactored the code to ensure modularity and maintainability.
- Updated the `Readme.md` with detailed instructions and project structure.
- Ensured compatibility with the `src` folder modules.
- Added support for marker files (e.g., `glasses.png`).

## Features Implemented
- Real-time face detection and glasses overlay.
- Hyper-realistic effects including dynamic lighting and 3D perspective.
- Support for multiple faces.
- Interactive features for toggling overlays.

## How to Test
1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Place the marker file (`glasses.png`) in the `assets/` directory.
5. Run the program using `python tools/ar_face_filter.py`.
6. Test the AR functionality with a webcam.

## Notes
- Ensure the `requirements.txt` dependencies are installed before running the project.
- The program has been tested on Windows and Linux.

## Future Improvements
- Add support for additional virtual objects.
- Enhance performance for low-end devices.
- Introduce a GUI for better user interaction.

---

Thank you for reviewing this pull request! Please let me know if there are any changes or improvements required.
