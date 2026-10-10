import os

def validate_document(file_path):

    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    if not file_path.endswith(".txt"):
        raise ValueError("Only .txt files are supported")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

def load_document(file_path):

    validate_document(file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    if not text.strip():
        raise ValueError("Document is empty")

    return {
        "doc_id": os.path.basename(file_path),
        "file_type": os.path.splitext(file_path)[1],
        "text": text
    }