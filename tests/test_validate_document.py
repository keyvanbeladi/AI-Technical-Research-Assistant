import pytest

from src.ingestion import validate_document


def test_validate_document_accepts_existing_txt_file(tmp_path):
    document = tmp_path / "document.txt"
    document.write_text("content", encoding="utf-8")

    assert validate_document(str(document)) is None


@pytest.mark.parametrize("file_path", [None, 123, b"document.txt"])
def test_validate_document_rejects_non_string_paths(file_path):
    with pytest.raises(TypeError, match="file_path must be a string"):
        validate_document(file_path)


def test_validate_document_rejects_non_txt_extension_before_file_lookup(tmp_path):
    missing_pdf = tmp_path / "missing.pdf"

    with pytest.raises(ValueError, match="Only .txt files are supported"):
        validate_document(str(missing_pdf))


def test_validate_document_rejects_missing_txt_file(tmp_path):
    missing_document = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError, match=f"File not found: {missing_document}"):
        validate_document(str(missing_document))


def test_validate_document_rejects_uppercase_txt_extension(tmp_path):
    document = tmp_path / "document.TXT"
    document.write_text("content", encoding="utf-8")

    with pytest.raises(ValueError, match="Only .txt files are supported"):
        validate_document(str(document))
