import os

def extract_text_from_files(folder_path):
    """
    Extracts text content from all .txt files in a given folder.

    Args:
        folder_path (str): The path to the folder containing the notes.

    Returns:
        dict: A dictionary where keys are filenames and values are their text content.
    """
    text_data = {}
    # Get a list of all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # Open the file and read its content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                text_data[filename] = content
    return text_data


def search_notes(notes_dict, keyword):
    """
    Searches for a keyword in the text content of the notes.

    Args:
        notes_dict (dict): A dictionary of notes (filename: content).
        keyword (str): The keyword to search for.

    Returns:
        dict: A dictionary of search results (filename: list of matching lines).
    """
    results = {}
    # Iterate over each file and its content
    for filename, content in notes_dict.items():
        matching_lines = []
        # Split the content into lines
        lines = content.splitlines()
        # Check each line for the keyword (case-insensitive)
        for line_number, line in enumerate(lines, start=1):
            if keyword.lower() in line.lower():
                # If found, store the line number and the line content
                matching_lines.append(f"Line {line_number}: {line.strip()}")

        if matching_lines:
            results[filename] = matching_lines
    return results