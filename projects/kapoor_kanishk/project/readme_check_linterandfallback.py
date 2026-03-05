import os
import argparse # Used to get command-line arguments and provide a CLI interface

# --- CONFIGURATION ---
# Define the checks we want to perform. Each check is a dictionary
# with a name, a suggestion, and a simple function that returns True if the check passes.
CHECKS = [
    {
        "name": "Has a Title",
        "suggestion": "A README should start with a main title (e.g., '# Project Name').",
        "check_function": lambda content: content.strip().startswith('# ')
    },
    {
        "name": "Has a Description",
        "suggestion": "A good README explains what the project does (ideally more than 2 lines).",
        "check_function": lambda content: len(content.strip().splitlines()) > 2
    },
    {
        "name": "Contains 'Installation' Section",
        "suggestion": "Should include a section on how to install the project (e.g., '## Installation').",
        "check_function": lambda content: '## installation' in content.lower()
    },
    {
        "name": "Contains 'Usage' Section",
        "suggestion": "Should include a section on how to use the project (e.g., '## Usage').",
        "check_function": lambda content: '## usage' in content.lower()
    },
    {
        "name": "Mentions a License",
        "suggestion": "An open-source project must specify a license (e.g., 'Licensed under MIT').",
        "check_function": lambda content: 'license' in content.lower()
    },
    {
        "name": "Has Contribution Guidelines",
        "suggestion": "Should tell others how to contribute (e.g., '## Contributing').",
        "check_function": lambda content: '## contributing' in content.lower() or '## contribution' in content.lower()
    }
]

# --- CORE LOGIC ---

def run_linter(file_path):
    """
    Reads a file and runs all defined checks against its content, then prints a report.
    """
    print(f"--- Analyzing '{file_path}' ---")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\n❌ ERROR: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"\n❌ ERROR: Could not read the file. Reason: {e}")
        return

    passed_checks = 0
    total_checks = len(CHECKS)
    
    print("\n[+] Running Checks...")
    # Run each check
    for item in CHECKS:
        # The check_function is called with the file content
        if item["check_function"](content):
            print(f"  ✅ PASSED: {item['name']}")
            passed_checks += 1
        else:
            print(f"  ❌ FAILED: {item['name']}")
            print(f"     └── Suggestion: {item['suggestion']}")

    # Print the final score
    score = (passed_checks / total_checks) * 100
    print("\n--- Linter Finished ---")
    print(f"Score: {passed_checks}/{total_checks} checks passed ({score:.2f}%)")


def run_demo_mode():
    """
    Creates a temporary demo README, runs the linter on it, and cleans up.
    """
    print("No file path provided. Running a built-in demo...")
    
    # Create a dummy README file for the demo with some missing sections
    demo_readme_content = """
# My Awesome Project

This is a short description of my project. It does amazing things.

## Usage
Here is how you use the project. Run `python project.py`.

## License
This project is licensed under the MIT License.
    """
    demo_filename = "DEMO_README.md"
    try:
        with open(demo_filename, "w", encoding='utf-8') as f:
            f.write(demo_readme_content)
        
        print(f"\nCreated a temporary demo file named '{demo_filename}'.\n")
        run_linter(demo_filename)
        
    finally:
        # Clean up the demo file
        if os.path.exists(demo_filename):
            os.remove(demo_filename)
            print(f"\nCleaned up temporary file '{demo_filename}'.")


# --- SCRIPT EXECUTION ---

if __name__ == "__main__":
    # This part allows the script to be run from the command line
    # with a file path, e.g., "python readme_check.py README.md"
    parser = argparse.ArgumentParser(
        description="A simple linter for README.md files to check for FOSS best practices.",
        epilog="If no file is provided, the script will run in demo mode."
    )
    parser.add_argument('file', nargs='?', default=None, help="Path to the README.md file to check.")
    args = parser.parse_args()

    if args.file:
        run_linter(args.file)
    else:
        # If no file is provided, run the DEMO
        run_demo_mode()
