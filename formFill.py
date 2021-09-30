import pdfrw
import datetime

#Input and output PDF forms
pdfIp = "simpleForm.pdf"
pdfOp = "FilledInForm.pdf"

fNameIn = "tempFirstName"
lNameIn = "tempLastName"
temperature = ""
dateToday = datetime.date.today()
print(dateToday)

ipPdf = pdfrw.PdfReader(pdfIp)
#print(ipPdf)

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

for page in ipPdf.pages:
    annotations = page[ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                #print(key)
