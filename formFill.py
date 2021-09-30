import pdfrw
import datetime
from flask import Flask, request, send_from_directory

# import json


app = Flask(__name__)

@app.route('/covidrequirements',methods = ['POST'])
def getCovidRequirements():
    return{
        "response": "In order to get the covid Form the following requirements must be met."
        #TO DO FILL IN REQUIREMENTS in this line and note the 
    }

@app.route('/covidform',methods = ['POST'])
def getCovidForm():
    pdfIp = "simpleForm.pdf"
    requestData = request.get_json()
    name = requestData['user']
    temperature = requestData['args']
    pdfOp = '{employeeName}-{date}.pdf'.format(employeeName= name, date = datetime.date.today())
    return{
        fillInFileData(name,temperature,pdfIp,pdfOp)
    }

#saving completed forum
@app.route('/pdf/<path:path>')
def send_js(path):
    return send_from_directory('pdf', path)

#gets the available fields in pdf
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

#Putting Data Into PDF
def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                    AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf) 

#Getting the data and running fucntion to fill in form
def fillInFileData(name,temp, template_input, template_output):
    data_dict = {
        
        'name': name,
        'temp': temp,
        'date': datetime.date.today(),
    }
    return fill_pdf(template_input, template_output, data_dict)      