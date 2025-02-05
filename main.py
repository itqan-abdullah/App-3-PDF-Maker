from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation='L',unit='mm',format="a4") 
pdf.set_auto_page_break(auto=False,margin=0)
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
    pdf.line(10,22,200,22)

    pdf.ln(170)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row['Topic'],align='R')
    #for i in range(2,12):
        #pdf.line(10,22*i,200,22*i)


    for i in range(int(row["Pages"]) - 1) :
       
        pdf.add_page()

        pdf.ln(170)
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row['Topic'],align='R')

        

pdf.output("output.pdf")

#pdf.add_page()

#pdf.set_font(family="Times", style='B', size=12)

#pdf.cell(w=0,h=12,txt="Hello There!",align='L',ln=1,border=1)


#