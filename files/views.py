from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import cm 
from django.http import HttpResponse

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
