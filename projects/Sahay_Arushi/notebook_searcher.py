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