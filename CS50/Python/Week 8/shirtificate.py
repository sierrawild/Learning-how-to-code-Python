import os
os.chdir(r"C:\Users\Pawel\Desktop\Learning how to code Python\CS50\Python\Week 8")

from fpdf import FPDF

cs50 = "CS50 Shirtificate"


class PDF(FPDF):
    def img(self):
        # img
        self.image("sirtificate.png", )
    