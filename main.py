# To create PDF documents
from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.add_page()
    print(row['Topic'], ":  ", row['Pages'])

    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, text=row['Topic'], align='L', new_x='LMARGIN', new_y='NEXT', border=1)
    pdf.set_font(family='Helvetica', style='I', size=10)
    pdf.cell(w=0, h=12, text='Pages: ' + str(row['Pages']) , align='L', new_x='LMARGIN', new_y='NEXT', border=1)


pdf.output('output.pdf')



