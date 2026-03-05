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

Multi-File Support: Can search content within .txt, .pdf, and common image file types (.png, .jpg, etc.).

Smart PDF Handling: Automatically detects if a PDF is text-based or image-based and uses the appropriate method to extract the content.

Optical Character Recognition (OCR): Uses an OCR engine to read text from image files and scanned PDFs.

Keyword Search: Allows users to search for a specific keyword or phrase.

Contextual Results: Displays search results with the filename, line number, and a snippet of the matching text.

Offline-First: The entire tool runs without an internet connection after the initial setup.
---

## Tech Stack
Language: Python

Libraries: os, PyPDF2, PyMuPDF, pytesseract, opencv-python
---

## How to Run
Ensure you have Python installed.

Install the necessary Python libraries by running the following command in your terminal:
pip install PyPDF2 PyMuPDF pytesseract opencv-python

Install the Tesseract OCR engine on your system.

Copy your .txt, .pdf, or image files into the sample_notes folder.

Run the program from the command line:
python notebook_searcher.py

The program will prompt you to enter a keyword to search (type q to quit).
---

## Project Structure

your-project/
├── notebook_searcher.py # Main project file
├── README.md            # This file
└── sample_notes/        # Place your notes here (.txt, .pdf, .jpg, etc.)
---

## Demo Screenshot / Output
Microsoft Windows [Version 10.0.26100.4946]
(c) Microsoft Corporation. All rights reserved.

C:\Users\DELL>cd C:\Users\DELL\Desktop\FOSS-Recruitment-2025\projects\Sahay_Arushi

C:\Users\DELL\Desktop\FOSS-Recruitment-2025\projects\Sahay_Arushi>python notebook_searcher.py

Enter a keyword to search (or type 'q' to quit): Void

--- Search Results ---

Found in Business law unit one.pdf:
  - Line 44: + distinguish between void, voidable and illegal contact; and
  - Line 369: From the point of view of enforceability a contract may be (i valid, (i) void,
  - Line 371: (Gi) voidable, (i) illegal or (v) unenforceable. These terms shall be used quite
  - Line 383: fone or more of these elements is/are missing, the contract is ether void,
  - Line 384: voidable, illegal oF unenforceable,
  - Line 386: |) Void Contract: According to Section 2 (j) A contract which ceases 10
  - Line 388: be enforceable by law Becomes void when it ceases to he enforceable.
  - Line 390: that a contract is not void from its inception. 1 is valid and binding upon
  - Line 392: reasons, it becomes unenforceable and so treated as void. A contract may
  - Line 393: become void due to impossibility of performance, change of law or some
  - Line 395: This contract becomes void on the death of B. A void contract should
  - Line 396: be distinguished from void agreement. Section 22) says that a”
  - Line 397: ‘agreement not enforceable by law is said to be void. In the ease of void
  - Line 399: rights on any person and creates no obligations. tis void absiitio ie,
  - Line 400: from the very beginning. For example an agreement with a minor is void
  - Line 403: Now it should be clear to you that a void agreement is not the same thing as
  - Line 404: avoid contract. Avoid agreement never matures into a contract, it is void from
  - Line 405: the very beginning. A void contract, on the other hand, was valid when it was
  - Line 407: void. A contract cannot be void ab-initio, itis only an agreement which
  - Line 408: cean be void al
  - Line 410: i) Voidable Contract: According to Section i) of the Contract Act, An
  - Line 412: parties thereon, bu not atthe option of the other oF others, is a voidable
  - Line 413: contract. Thus, a voidable contract is one which can be set aside or
  - Line 415: avoided by the party entitled to do so, it remains a valid contract. A
  - Line 416: contract is usually treated as voidable when the consent of party has not
  - Line 418: misrepresentation or fraud. The contract is voidable at the option of the
  - Line 422: 's voidable at the option of B, the aggrieved party. If however, B does not
  - Line 425: matter for some consideration, the contract eannot be avoided. For example,
  - Line 429: contract cannot be avoided. You should note that the option to set aside
  - Line 432: enforceable by law. IPhowever, the agurieved party avoids the contract,
  - Line 434: if the party avoiding the contract has received any benefit under the
  - Line 438: Distinetion between Void Agreement and Voidable Contract
  - Line 440: Void Agreement Voidable Contract
  - Line 441: 1) Itis void from the very 1) Ie remains valid cil tis repudiated
  - Line 443: 2) Accontract is void if any —_-2)_A contract is voidable if the consent
  - Line 452: before the contract is avoided.
  - Line 453: 5) Lapse of time will not make it 5) If tis not avoided within reasonable
  - Line 455: remains void.
  - Line 472: ‘The term “illegal agreement’ is wider than the term “void agreement All
  - Line 473: illegal agreements are void but all void agreements are not
  - Line 475: ‘minor Le. void but i is not illegal because the object of this agreement is
  - Line 477: void agreement relates to their effect on the transactions which are collateral
  - Line 479: agreements become void. For example, A engages B to shoot C. To
  - Line 484: ‘agreement is algo void. D cannot recover the money from A. Take another
  - Line 486: to B. Here the main agreement is void (not illegal). Hence the agreement
  - Line 494: are also void but the transactions collateral to void agreements are not
  - Line 497: Difference between Void Agreement and Hlegal Agreement
  - Line 501: 1) Allvoid agreements are not 1) All ill
  - Line 504: agreements are void.
  - Line 508: void agreement are not agreements are abo alfected ie,
  - Line 509: alfected ic. they do not they also become void
  - Line 510: become void
  - Line 512: 3) Ia contract becomes void 3) The money advanced or thing given
  - Line 543: Valid Void Voidable Tegal] Tinentorceabe
  - Line 549: 1) What is a void contract?
  - Line 551: 2) When is a contract voidable?
  - Line 576: the scooter was not new. Can B avoid the contract?
  - Line 592: declared to be void. Thus, at agreement becomes a valid contract i it has the
  - Line 606: 7) Agreement not expressly declared void
  - Line 668: of the first four factors, the contrat would be voidable atthe option ofthe
  - Line 670: is material to the agreement, it would be void. You will larn about free
  - Line 726: is void because the object of the agreement is unlawful Ifthe object is
  - Line 728: shall be void. Thus, the consideration as well as the object, of the
  - Line 731: Agreement not expressly declared void: The agreement must not have
  - Line 732: been expressly declared void under Contract Act. Sections 24 to 30
  - Line 734: void, They are agreement in restraint of marriage, agreement in restraint of
  - Line 741: declared void under Section 26,
  - Line 745: have been expressly declared void by the Contract Aet, no power on earth
  - Line 750: ‘made certain, are void. Thus to make a valid contract it is absolutely
  - Line 763: in itself is void (Section $6). If the act is impossible of performance,
  - Line 807: enforceability it may be a valid, void, voidable, illegal or unenforceable contact.
  - Line 809: ‘An agreement not enforceable by law is said to be a “void agreement’. The
  - Line 810: term “Void contract” refers 1o an agreement which was valid when it was
  - Line 811: entered into but become void later on because of one reason or the other. A
  - Line 812: “voidable contract’ is one which is voidable (can be avoided) atthe option of
  - Line 814: where the objector the consideration is unlawful. Such agreement is also void
  - Line 867: Void Agreement: An agreement not enforceable by law:
  - Line 869: Void ab-initio: Something which is void from the very beginning,
  - Line 871: Void Contract: An agreement which was valid when entered into but which
  - Line 872: subsequently becomes void.
  - Line 874: Voidable Contract: A contract which can be avoided at the option of the
  - Line 883: 5) i) No ii) contract becomes void ii) No iv) Yes v) No
  - Line 903: |) Void and Voidable contracts,
  - Line 904: i) Void and Hlegal agreements
--------------------

Enter a keyword to search (or type 'q' to quit):

---

## AI Tools Used
I used ChatGPT and Gemini for this project. It helped with:

Code Snippets and Logic: I brainstormed a few ideas myself, tried to incorporate a few logic flows from what I had understood in my previous attempt and confirmed if it was the right thinking. I asked for small code snippets to learn from and incorporated them into my own code.

Debugging: It assisted with understanding errors and finding solutions.



---

## Future Improvements
Regex Search: Allow users to perform more powerful searches using regular expressions.

GUI: Develop a simple graphical user interface to make the tool more user-friendly.


---

## Notes for Reviewers
This project is designed to be fully offline after the initial setup, respecting the FOSS recruitment guidelines. It requires the Tesseract OCR engine to be installed on the system to function correctly.


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

