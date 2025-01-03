# To create PDF documents
from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    for page in range(row['Pages']):
        pdf.add_page()
        print(row['Topic'], ":  ", row['Pages'])

        # Header
        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(100,100,100) # grey
        pdf.cell(w=0, h=12, text=row['Topic'], align='L', new_x='LMARGIN', new_y='NEXT')
        pdf.line(10, 22, 200, 22 )
        # pdf.set_font(family='Helvetica', style='I', size=10)
        # pdf.cell(w=0, h=12, text='Pages: ' + str(row['Pages']) , align='L', new_x='LMARGIN', new_y='NEXT', border=0)

        # Body
        for i in range(40, 270, 12):
            pdf.set_draw_color(210, 210, 210)
            pdf.line(10, i, 200, i)

        # Footer
        pdf.set_y(-15)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_draw_color(170, 170, 170)
        pdf.line(10, 280, 200, 280)
        pdf.set_text_color(170, 170, 170)
        pdf.cell(w=0, h=8, text=str(row['Topic']) , align='R', border=0) # , new_x='RMARGIN', new_y=YPos.BMARGIN,

pdf.output('output.pdf')



