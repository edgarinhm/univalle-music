'''
Created on Oct 22, 2012

@author: edgar
'''
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table , TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.platypus import XPreformatted
from cStringIO import StringIO

class Reportes(object):
    
    def generarPdf(self, output):

        filename = 'univalle-music-reportes.pdf'
        output['Content-Disposition'] = 'filename=' + filename
        
        doc = SimpleDocTemplate(output, pagesize=A4,
              rightMargin=.5 * inch, leftMargin=.5 * inch,
              topMargin=inch, bottomMargin=.5 * inch)

        OutlinePDF = []
        styles = getSampleStyleSheet()
        OutlinePDF.append(Paragraph("<b>Grading:</b>",
                  styles['Heading1']))
        OutlinePDF.append(Spacer(1, 12))
        doc.build(OutlinePDF)
        #def preformat_html_textarea(value, endwidth=135):
#    import textwrap
#    new_value = value.replace('\r', '')
#    new_values = new_value.split('\n')
#    result = ""
#    for line in new_values:
#        result += textwrap.fill(line, endwidth) + "\n"
#
#    return result