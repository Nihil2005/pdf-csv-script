from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from random import choice, randint
import os

# Sample data for generating random PDFs
drug_brands = ["BrandA", "BrandB", "BrandC", "BrandD"]
generic_names = ["GenericA", "GenericB", "GenericC", "GenericD"]
compositions = ["CompositionA", "CompositionB", "CompositionC", "CompositionD"]
dosages = ["50mg", "100mg", "200mg", "500mg"]
manufacturers = ["ManufacturerX", "ManufacturerY", "ManufacturerZ", "ManufacturerW"]
expiration_dates = ["2025-01-01", "2024-12-31", "2026-06-30", "2025-11-15"]

def generate_random_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Generate random drug details
    drug_brand_name = choice(drug_brands)
    generic_name = choice(generic_names)
    drug_composition = choice(compositions)
    dosage = choice(dosages)
    manufacturer = choice(manufacturers)
    expiration_date = choice(expiration_dates)

    # Write text to the PDF
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Drug Brand Name: {drug_brand_name}")
    c.drawString(100, height - 130, f"Generic Name: {generic_name}")
    c.drawString(100, height - 160, f"Drug Composition: {drug_composition}")
    c.drawString(100, height - 190, f"Dosage: {dosage}")
    c.drawString(100, height - 220, f"Manufacturer: {manufacturer}")
    c.drawString(100, height - 250, f"Expiration Date: {expiration_date}")

    # Add additional description
    c.setFont("Helvetica-Oblique", 10)
    description = (
        "This document provides detailed information about the drug listed above. "
        "Ensure to follow the dosage instructions as per the guidelines. "
        "For further inquiries, contact the manufacturer directly."
    )
    c.drawString(100, height - 280, description)

    # Save the PDF file
    c.save()

def generate_multiple_pdfs(num_files, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_files):
        filename = os.path.join(output_folder, f"random_drug_{i+1}.pdf")
        generate_random_pdf(filename)
        print(f"PDF '{filename}' has been created.")

if __name__ == "__main__":
    num_files = 100
    output_folder = "pdf_files"
    generate_multiple_pdfs(num_files, output_folder)
