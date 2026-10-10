import pytest

from src.ingestion import load_document


def test_load_valid_document():

    document = load_document("data/raw/materials_science.txt")

    assert document["doc_id"] == "materials_science.txt"
    assert document["file_type"] == ".txt"
    assert document["text"]


def test_load_missing_document():

    with pytest.raises(FileNotFoundError):
        load_document("data/raw/not_existing.txt")


def test_load_unsupported_file_type(tmp_path):

    file_path = tmp_path / "document.pdf"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Sample content")

    with pytest.raises(ValueError, match="Only .txt files are supported"):
        load_document(str(file_path))


def test_load_empty_document(tmp_path):

    file_path = tmp_path / "empty.txt"

    with open(file_path, "w", encoding="utf-8"):
        pass

    with pytest.raises(ValueError, match="Document is empty"):
        load_document(str(file_path))