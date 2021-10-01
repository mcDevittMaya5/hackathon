from reportlab.pdfgen import canvas

from reportlab.lib.colors import black,white

def create_simple_form():
    c = canvas.Canvas('simpleForm.pdf')
    
    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Ireland COVID-19 Healthy Workplace Policy')
    c.setFont("Courier", 14)
    form = c.acroForm
    
    c.drawString(15, 650, 'Employee Name:')
    form.textfield(name='name', tooltip='Name',
                   x=150, y=635, borderStyle='inset',
                   borderColor=black, fillColor=white, 
                   width=300,
                   textColor=black, forceBorder=True)

    c.drawString(15, 560, 'This Employee has not had symptoms of cough, fever,high temperature,')
    c.drawString(15, 550, 'sore throat,runny nose, breathlessness or flu like')
    c.drawString(15, 540, 'symptoms now or for the past 14 days.')
    
    c.drawString(15, 500, 'This Employee has not been diagnosed with, or suspected to have had,')
    c.drawString(15, 490, 'a Covid-19 infeaction in the last 14 days.')
    
    c.drawString(15, 450, 'This Employee has not been a close contact in the last 14 days.')
    
    c.drawString(15, 410, 'This Employee has not been advised by a doctor to self-isolate')
    c.drawString(15, 400, 'or cacoon.')
    
    c.drawString(15, 370, 'This Employee is not waiting for the result of a covid-19 test.')
    
    c.drawString(15, 330, 'Temperature:')
    form.textfield(name='temp', tooltip='Temp',
                   x=110, y=320, borderStyle='inset',
                   borderColor=black, fillColor=white,
                   forceBorder=True)
    
    c.drawString(300, 330, 'Date:')
    form.textfield(name='date', tooltip='date',
                   borderColor=black, fillColor=white,
                   x=350, y=320, borderStyle='inset',
                   forceBorder=True)
    
    c.save()
    
if __name__ == '__main__':
    create_simple_form()
