#!usr/evn python
#-*-coding:utf8-*-
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import cm
import csv
import re
from django.utils.encoding import smart_str
from django.http import HttpResponse
import xlwt

from django.template import Context
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
import datetime
import time
from django.utils import timezone
from datetime import datetime
from files.forms import UploadFileForm
from files.models import Car

ROOT_PATH = '/static/img/headimg/'

def home(request):
    file_name = datetime.now().strftime('%Y%m%d%H%M%S')
    if request.method=="POST":
        photo = request.FILES['file']
        p_name, format = photo.name.split('.')
        photo.name=file_name+'.'+format
        car = Car(name=photo.name, photo=photo)
        car.save()
    else:
        form = UploadFileForm()

    car = Car.objects.all()
    car_content = []
    for c in car:
        car_content.append({
            'c_name': c.name,
            'c_url': ROOT_PATH+c.name,
        })
    return render_to_response('files/home.html',
        locals(),
        context_instance=RequestContext(request)
        )


def export_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; "filename="hello.pdf"'

    buffer = BytesIO()
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(9*cm, 22*cm, "Hello World.nimei")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    print pdf,'nooooooooooooooooo'
    buffer.close()
    response.write(pdf)
    return response


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="CSV.csv"'

    writer = csv.writer(response)
    writer.writerow(['name studentID'])
    writer.writerow(['yinshiyong 20101472'])

    return response


def export_xls(request):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.num_format_str = 'D-MMM-YY'

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 'Test', style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))
    fname = 'ex.xls'
    agent=request.META.get('HTTP_USER_AGENT') 
    if agent and re.search('MSIE',agent):
        response =HttpResponse(mimetype="application/vnd.ms-excel") #解决ie不能下载的问题
        response['Content-Disposition'] ='attachment; filename=%s' % urlquote(fname) #解决文件名乱码/不显示的问题
    else:
        response =HttpResponse(mimetype="application/ms-excel")#解决ie不能下载的问题
        response['Content-Disposition'] ='attachment; filename=%s' % smart_str(fname) #解决文件名乱码/不显示的问题
    wb.save(response)#this is the key
    return response
