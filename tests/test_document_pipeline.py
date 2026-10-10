
from src.ingestion import load_document
from src.chunking import chunk_text


def test_load_and_chunk_document():

    document = load_document("data/raw/materials_science.txt")

    chunks = chunk_text(
        document["text"],
        chunk_size=200,
        overlap=40
    )

    assert len(chunks) > 1
    assert all(chunk.strip() for chunk in chunks)
    assert all(len(chunk) <= 200 for chunk in chunks)

    reconstructed_text = chunks[0]

    for chunk in chunks[1:]:
        reconstructed_text += chunk[40:]

    assert reconstructed_text == document["text"]