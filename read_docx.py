#!/usr/bin/env python3
"""
read_docx.py
Extracts clean text from docx file using built-in zipfile & xml modules.
"""

import sys
import zipfile
import xml.etree.ElementTree as ET

def extract_text(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read("word/document.xml")
    root = ET.fromstring(xml_content)
    
    paragraphs = []
    for p in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
        texts = [node.text for node in p.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t") if node.text]
        if texts:
            paragraphs.append("".join(texts))
    return "\n\n".join(paragraphs)

if __name__ == "__main__":
    fpath = "/Users/deepankarakasajoo/My Drive/Family1stLegacy/Spanish Update/Family_First_Legacy_FINAL_CLEAN_Spanish.docx"
    text = extract_text(fpath)
    with open("/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy/extracted_spanish_doc.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted {len(text)} chars to extracted_spanish_doc.txt")
