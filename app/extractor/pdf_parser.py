import fitz  # PyMuPDF

def is_heading(text, font_size, y0, font_flags):
    # Heuristics to detect a heading
    return (
        font_size >= 13 and
        len(text.split()) < 10 and
        text.istitle() and
        y0 < 200  # appears high on the page
    ) or (
        font_flags == 20  # bold & upright, varies per font
    ) or (
        text.isupper() and len(text) < 40
    )

def extract_chunks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []

    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue

            text = ""
            max_font_size = 0
            y0 = 1000
            font_flags = 0

            for line in block["lines"]:
                for span in line["spans"]:
                    content = span["text"].strip()
                    if content:
                        text += content + " "
                        if span["size"] > max_font_size:
                            max_font_size = span["size"]
                            y0 = span["origin"][1]
                            font_flags = span.get("flags", 0)

            cleaned_text = text.strip()
            if len(cleaned_text) < 10:
                continue

            chunk_type = "heading" if is_heading(cleaned_text, max_font_size, y0, font_flags) else "paragraph"

            chunks.append({
                "text": cleaned_text,
                "type": chunk_type,
                "page": page_number,
                "font_size": max_font_size,
                "y0": y0
            })

    return chunks
