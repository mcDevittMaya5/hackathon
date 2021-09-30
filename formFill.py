#https://akdux.com/python/2020/10/31/python-fill-pdf-files.html#PDF-Setup
import pdfrw
import datetime
import requests

#gets the available fields in pdf
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# for page in ipPdf.pages:
#     annotations = page[ANNOT_KEY]
#     for annotation in annotations:
#         if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
#             if annotation[ANNOT_FIELD_KEY]:
#                 key = annotation[ANNOT_FIELD_KEY][1:-1]
#                 print(key)
               
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
                
def fillInFileData(data, template_input, template_output):
    data_dict = {
        
        'fname': data.get('fname', ''),
        'lname': data.get('lname', ''),
        'temp': data.get('temp',''),
        'date': data.get('date',''),
    }
    
    return fill_pdf(template_input, template_output, data_dict)      


if __name__ == '__main__':
    
    #Input and output PDF forms
    pdfIp = "simpleForm.pdf"
    pdfOp = "FilledInForm.pdf"
    
    #ipPdf = pdfrw.PdfReader(pdfIp)
    #print(ipPdf)
    
    data_dict = {
    'fname': 'Jane',
    'lname':'Doe',
    'temp':'37',
    'date' : datetime.date.today(),
    }
    
    fillInFileData(data_dict, pdfIp, pdfOp)