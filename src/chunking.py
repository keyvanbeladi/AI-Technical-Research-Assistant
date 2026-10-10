
def chunk_text(text, chunk_size=1000, overlap=200):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        raise ValueError("text cannot be empty")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)

        if end < text_length:
            boundary = text.rfind("\n\n", start + overlap, end)

            if boundary != -1 and boundary + 2 <= end:
                end = boundary + 2

        chunks.append(text[start:end])

        if end >= text_length:
            break

        start = end - overlap

    return chunks