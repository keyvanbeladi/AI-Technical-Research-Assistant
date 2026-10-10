
import pytest

from src.chunking import chunk_text


def test_chunk_text_without_overlap():

    text = "ABCDEFGHIJ"

    chunks = chunk_text(text, chunk_size=4, overlap=0)

    assert chunks == ["ABCD", "EFGH", "IJ"]


def test_chunk_text_with_overlap():

    text = "ABCDEFGHIJ"

    chunks = chunk_text(text, chunk_size=4, overlap=2)

    assert chunks == ["ABCD", "CDEF", "EFGH", "GHIJ"]


def test_chunk_text_empty_input():

    with pytest.raises(ValueError, match="text cannot be empty"):
        chunk_text("")


def test_chunk_size_must_be_positive():

    with pytest.raises(ValueError, match="chunk_size must be greater than zero"):
        chunk_text("ABCDEFGHIJ", chunk_size=0)


def test_overlap_must_be_smaller_than_chunk_size():

    with pytest.raises(ValueError, match="overlap must be smaller than chunk_size"):
        chunk_text("ABCDEFGHIJ", chunk_size=4, overlap=4)


def test_chunk_text_preserves_paragraphs_when_possible():

    text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."

    chunks = chunk_text(text, chunk_size=40, overlap=0)

    assert chunks == [
        "First paragraph.\n\nSecond paragraph.\n\n",
        "Third paragraph."
    ]


def test_chunk_text_respects_chunk_size_with_overlap():

    text = "A" * 50

    chunks = chunk_text(text, chunk_size=20, overlap=5)

    assert all(len(chunk) <= 20 for chunk in chunks)