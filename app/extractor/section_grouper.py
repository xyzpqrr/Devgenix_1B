def group_chunks_into_sections(chunks):
    """
    Groups paragraph chunks under their preceding heading.
    Adds document name based on first chunk in each section.
    """
    sections = []
    current_section = {
        "title": "Untitled Section",
        "page": 1,
        "content": "",
        "chunk_count": 0,
        "document": chunks[0]["document"] if chunks else "unknown"
    }

    for chunk in chunks:
        if chunk["type"] == "heading":
            if current_section["chunk_count"] > 0:
                current_section["content"] = current_section["content"].strip()
                sections.append(current_section)

            current_section = {
                "title": chunk["text"],
                "page": chunk["page"],
                "content": "",
                "chunk_count": 0,
                "document": chunk.get("document", "unknown")
            }

        elif chunk["type"] == "paragraph":
            current_section["content"] += chunk["text"].strip() + " "
            current_section["chunk_count"] += 1
            if current_section["chunk_count"] == 1:
                current_section["document"] = chunk.get("document", "unknown")

    if current_section["chunk_count"] > 0:
        current_section["content"] = current_section["content"].strip()
        sections.append(current_section)

    return sections
