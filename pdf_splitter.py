import os
from PyPDF2 import PdfReader, PdfWriter

# Function to split PDF into individual pages
def split_pdf(input_pdf_path, output_folder):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        # Iterate through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Create a PdfWriter object for each page
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # Define the output file path
            output_pdf_path = os.path.join(output_folder, f'page_{page_num + 1}.pdf')
            
            # Write the single page to a new PDF file
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)
                
            print(f'Saved: {output_pdf_path}')

# Specify the path to the input PDF file and output folder
input_pdf_path = "E:\Petition Copy.pdf"  # Replace with your PDF file path
output_folder = "split_pages"    # Folder to save the split pages

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Split the PDF into individual pages
split_pdf(input_pdf_path, output_folder)
