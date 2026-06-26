import os
os.chdir(r"C:\Users\Pawel\Desktop\Learning how to code Python\CS50\Python\Week 8")

from fpdf import FPDF

cs50 = "CS50 Shirtificate"
name = input('Name: ').strip()

pdf = FPDF(orientation="portrait", unit='mm', format='A4')

pdf.add_page()
pdf.set_font('Arial', size=46, style='B')

# width of page and text
page_w = pdf.w

# printing text on the top
pdf.cell(0, 50, cs50, align="C", ln=True)

# image
pdf.image('shirtificate.png', page_w * 0.05, 80, page_w * 0.9)

# text on the shirt
pdf.set_font('Arial', size=26, style='B')
pdf.set_text_color(255,255,255)

pdf.cell(0, 150, name + ' took CS50', align="C")

# saving the document
pdf.output("shirtificate.pdf")
