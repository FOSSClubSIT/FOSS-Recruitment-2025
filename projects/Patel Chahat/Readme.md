# Project Title: Write your project name here

## Student Details
- **Name**: Chahat Chetankumar Patel 
- **PRN**: 24070126047  
- **Year**: SY 
- **Branch**: AIML  

---

## Problem Statement
A simple blockchain system that securely records and validates transactions using cryptographic hashes.  


---

## Features

- Add new transactions as blocks
- Display the blockchain in readable format
- Validate integrity of the chain
- Reset blockchain with a fresh genesis block
- Persistent storage in JSON file 

---

## Tech Stack
- Language: Python
- Libraries: argparse, json, hashlib, time, os

---

## How to Run
1. Open the folder in VS Code.  
2. Run the following commands:  

    ```bash
    I. python main.py add "Mr.Zoro Bob 10 coins" 
    II.python main.py show 
    III.python main.py validate 
    IV.python main.py reset 



---

## Project Structure
mini-blockchain/
├── main.py
├── mini_blockchain/
│   ├── __init__.py
│   ├── block.py
│   ├── blockchain.py
│   ├── utils.py
│   └── data/
│       └── chain.json
└── README.md





## Demo Screenshot / Output
Add a screenshot of your project running, or copy-paste sample terminal output here.

---

## AI Tools Used
ChatGPT and Gemini(for guidance & code fixes)

---

## Future Improvements
- Add Proof-of-Work (mining) for block validation
- Add a Flask API to interact with blockchain via HTTP
- Add a peer-to-peer network for multiple nodes
- Implement digital signatures for transactions


---

## Notes for Reviewers
- Project runs completely offline.
- Blockchain is persisted in data/chain.json.

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

