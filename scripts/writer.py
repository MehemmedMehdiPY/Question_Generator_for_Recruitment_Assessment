"""The following code is generated by Claude 3.5 Sonnet"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from textwrap import wrap
import os

def text_to_pdf(input_text, font_size=12, margin=72):
    """
    Convert text to PDF file.
    
    Parameters:
    input_text (str): The text to convert
    output_filename (str): Name of the output PDF file
    font_size (int): Font size to use
    margin (int): Page margin in points (72 points = 1 inch)
    """
    
    # The following code is created by the author
    output_filename='./output/output.pdf'
    if not os.path.exists("output"):
        os.makedirs("output")   
    # The end of human-generated code

    # Create a new PDF with the specified filename
    c = canvas.Canvas(output_filename, pagesize=letter)
    
    # Get page width and height
    width, height = letter
    
    # Set font and size
    c.setFont("Helvetica", font_size)
    
    # Calculate text width and height
    line_height = font_size * 1.2
    text_width = width - 2 * margin
    
    # Split text into lines that fit within the page width
    lines = []
    for text in input_text.split('\n'):
        # Wrap text to fit within margins
        wrapped_lines = wrap(text, width=int(text_width/font_size*1.75))
        lines.extend(wrapped_lines)
    
    # Initialize y position for text
    y = height - margin
    
    # Add text to PDF
    for line in lines:
        # If we've reached the bottom margin, create a new page
        if y < margin:
            c.showPage()
            y = height - margin
            c.setFont("Helvetica", font_size)
        
        # Add the line of text
        c.drawString(margin, y, line)
        y -= line_height
    
    # Save the PDF
    c.save()

# Example usage
if __name__ == "__main__":
    # Sample text
    sample_text = """This is a sample text that will be converted to PDF.
    It can handle multiple lines and will automatically wrap text that is too long to fit on one line.
    The text will flow onto new pages as needed."""
    
    # Convert text to PDF
    text_to_pdf(sample_text, 'example.pdf')