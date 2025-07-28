import json
import os
from datetime import datetime

def build_output_json(input_json, ranked_sections):
    metadata = {
        "input_documents": [doc["filename"] for doc in input_json["documents"]],
        "persona": input_json["persona"]["role"],
        "job_to_be_done": input_json["job_to_be_done"]["task"],
        "processing_timestamp": datetime.now().isoformat()
    }

    extracted_sections = []
    sub_section_analysis = []

    for i, section in enumerate(ranked_sections):
        extracted_sections.append({
            "document": section.get("document", "unknown"),
            "page_number": section["page"],
            "section_title": section["title"],
            "importance_rank": i + 1
        })

        sub_section_analysis.append({
            "document": section.get("document", "unknown"),
            "refined_text": section.get("summary", ""),  # Now pulls summary directly
            "page_number": section["page"]
        })

    return {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    }

def save_json(data, path="output/final_output.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
