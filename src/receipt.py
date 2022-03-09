# Very Simple receipt generation

from fpdf import FPDF
import os

def generate_receipt(item: str, date: str, amount: str, name: str, phone: str, email: str, address: str):

    pdf = FPDF('P', 'mm', 'A5')

    pdf.add_page()

    # Company Name and Receipt Heading
    pdf.set_font('times', 'B', 11)
    pdf.cell(40,10, "Task Software Inc",  border=0)

    pdf.set_font('times', 'BU', 18)
    pdf.cell(40,10, "Receipt", border=0, center=True)

    pdf.set_font('times',"", 11)
    pdf.cell(0,10, f'{date}', ln=1, align="R")
    pdf.set_font('times', 'BU', 15)
    pdf.cell(10,10, "Purchase by: ")
    pdf.set_font('times', 'B', 13)
    pdf.cell(10,10, f'{name}', center=True, ln=1)
    pdf.cell(10,10, f'{address}', center=True, ln=1)
    pdf.cell(10,10, f'{phone}', center=True, ln=1)
    pdf.cell(10,10, f'{email}', center=True, ln=1)
    pdf.cell(60,10, 'purchase', border=1)
    pdf.cell(80,10, f'{item}', border=1, ln=1)
    
    pdf.cell(0,10, "License cost: ", align='L')
    pdf.cell(0,10, f'{amount}', align="R")

    pdf.output(f'receipts/{phone}.pdf')
