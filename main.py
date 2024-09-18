from docx import Document

def replace_paragraph(doc_path):
    # Load the document
    doc = Document(doc_path)
    
    # Iterate through paragraphs and replace the target text
    for paragraph in doc.paragraphs:
        # if target_text in paragraph.text:
            # Replace only the target text while preserving the rest of the paragraph formatting
        # paragraph.text = paragraph.text.replace(paragraph.text, paragraph.text)
        pass
    
    # Save the modified document
    doc.save(doc_path)

# Example usage
replace_paragraph('input.docx')
