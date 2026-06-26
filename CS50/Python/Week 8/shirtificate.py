import os
os.chdir(r"C:\Users\Pawel\Desktop\Learning how to code Python\CS50\Python\Week 8")

from fpdf import FPDF

cs50 = "CS50 Shirtificate"
name = 'Pawel Babiak'

pdf = FPDF(orientation="portrait", unit='mm', format='A4')

pdf.add_page()
pdf.set_font('Arial', size=46, style='B')

# width of page and text
page_w = pdf.w
text_w = pdf.get_string_width(name)
text_center = page_w / 2 - text_w / 2
# print(f"{page_w=}\n{text_w=}\n{text_center=}") # debugging

# printing text
pdf.cell(0, 50, cs50, align="C")

# image
pdf.image('shirtificate.png', page_w * 0.05, 80, page_w * 0.9)

# text on the shirt
pdf.set_font('Arial', size=26, style='B')
# pdf.set_text_color(255,255,255)
pdf.cell(-text_center, 250, name, align="C")

# saving the document
pdf.output("Sirtificate.pdf")
