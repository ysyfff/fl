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
from xlrd import *
import os
from fl.settings import up_path
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
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
import time
from django.utils import timezone
from datetime import datetime
from files.forms import UploadFileForm
from files.models import Car

ROOT_PATH = '/static/img/headimg/'

def home(request):
    return render_to_response('files/home.html',
        locals(),
        context_instance=RequestContext(request)
        )

def export_fl(request):
    return render_to_response('files/export.html',
        locals(),
        context_instance=RequestContext(request)
        )

def import_img(request):
    file_name = datetime.now().strftime('%Y%m%d%H%M%S')
    if request.method=="POST":
        return HttpResponseRedirect('/')
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
    return render_to_response('files/import.html',
        locals(),
        context_instance=RequestContext(request)
        )


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; "filename="hello.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(response)

    p.drawString(9*cm, 22*cm, "Hello World.nimei")

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

    ws.write(0, 1, 'Test', style0)
    ws.write(1, 1, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))
    fname = 'ex.xls'
    agent=request.META.get('HTTP_USER_AGENT') 
    print agent
    if agent and re.search('MSIE',agent):
        response =HttpResponse(mimetype="application/vnd.ms-excel") 
        response['Content-Disposition'] ='attachment; filename=%s' % urlquote(fname)
    else:
        response =HttpResponse(mimetype="application/ms-excel")#解决ie不能下载的问题
        response['Content-Disposition'] ='attachment; filename=%s' % smart_str(fname)
    wb.save(response)#this is the key
    return response

def read_xls(request):
    xls_path = str(up_path+'/static/xls/')
    wb = open_workbook(str(xls_path+'example.xls'))
    for s in wb.sheets():
        print 'Sheet:', s.name
        content = []
        for row in xrange(s.nrows):
            row_con = []
            for col in xrange(s.ncols):
                row_con.append(s.cell(row, col).value)
            content.append(row_con)
    return render_to_response('files/read.html',
        locals(),
        context_instance=RequestContext(request)
        )
