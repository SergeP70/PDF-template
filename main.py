# To create PDF documents
from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    for page in range(row['Pages']):
        pdf.add_page()
        print(row['Topic'], ":  ", row['Pages'])

        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(100,100,100) # grey
        pdf.cell(w=0, h=12, text=row['Topic'], align='L', new_x='LMARGIN', new_y='NEXT')
        pdf.line(10, 22, 200, 22 )
        pdf.set_font(family='Helvetica', style='I', size=10)
        pdf.cell(w=0, h=12, text='Pages: ' + str(row['Pages']) , align='L', new_x='LMARGIN', new_y='NEXT', border=0)

pdf.output('output.pdf')



