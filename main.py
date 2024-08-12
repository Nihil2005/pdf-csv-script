import os
import fitz  # PyMuPDF
import re
import pandas as pd

# Function to extract text from the first page of a PDF
def extract_text_from_first_page(pdf_path):
    pdf_document = fitz.open(pdf_path)
    first_page = pdf_document[0]
    text = first_page.get_text()
    return text

# Function to extract required data from text
def extract_data_from_text(text):
    # Assuming that these patterns exist in the text, you may need to adjust regex patterns
    drug_brand_name = re.search(r'Drug Brand Name:\s*(.+)', text)
    generic_name = re.search(r'Generic Name:\s*(.+)', text)
    drug_composition = re.search(r'Drug Composition:\s*(.+)', text)
    
    # Use empty strings if regex search fails
    drug_brand_name = drug_brand_name.group(1) if drug_brand_name else 'N/A'
    generic_name = generic_name.group(1) if generic_name else 'N/A'
    drug_composition = drug_composition.group(1) if drug_composition else 'N/A'
    
    return drug_brand_name, generic_name, drug_composition

# Main function to process PDF files
def process_pdfs(pdf_folder, output_csv):
    data = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            text = extract_text_from_first_page(pdf_path)
            drug_brand_name, generic_name, drug_composition = extract_data_from_text(text)
            data.append([filename, drug_brand_name, generic_name, drug_composition])
            print(f'Processed {filename}')

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data, columns=['Filename', 'Drug Brand Name', 'Generic Name', 'Drug Composition'])
    df.to_csv(output_csv, index=False)
    print(f'Data saved to {output_csv}')

if __name__ == '__main__':
    pdf_folder = 'pdf_files'
    output_csv = 'output.csv'
    process_pdfs(pdf_folder, output_csv)
