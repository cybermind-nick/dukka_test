from multiprocessing import dummy
from turtle import right
from fpdf import FPDF

dummyMap = {
    "date": "March 30, 2022", "name": "Nicholas Ifeajika",
    "address": "my house","phone": "08137570097",
    "items": {"item1": "$10,000", "item2": "$20,000"} 
    }

def generate_receipt(obj):

    pdf = FPDF('P', 'mm', 'A5')

    pdf.add_page()

    # Company Name and Receipt Heading
    pdf.set_font('times', 'B', 11)
    pdf.cell(40,10, "Task Software Inc",  border=True)

    pdf.set_font('times', 'BU', 18)
    pdf.cell(40,10, "Receipt", border=True, center=True)
    # pdf.cell()

    # add an actual database call to retrieve the purchase data
    pdf.set_font('times',"", 11)
    pdf.cell(10,10, f'{obj["date"]}', ln=1, align="r")
    pdf.set_font('times', 'BU', 15)
    pdf.cell(10,10, "Purchase by: ")
    pdf.set_font('times', 'BU', 13)
    pdf.cell(10,10, f'{obj["name"]}', center=True, ln=1)
    pdf.cell(10,10, f'{obj["address"]}', center=True, ln=1)
    pdf.cell(10,10, f'{obj["phone"]}', center=True, ln=1)
    pdf.cell(80,10, 'item')
    pdf.cell(80,10, 'Amount', ln=1)
    for k in obj["items"]:
        pdf.cell(80,10, f'{k}')
        pdf.cell(80,10, f'{obj["items"][k]}', ln=1)
        # now for items
        # for i in dummyMap["items"]:



    pdf.output('test.pdf')

generate_receipt(dummyMap)