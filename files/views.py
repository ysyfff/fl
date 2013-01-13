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
from files.forms import UploadFileForm
from files.models import Car

def home(request):
    if request.method=="POST":
        photo = request.FILES['file']
        car = Car(name="aaa", price=12, photo=photo)
        car.save()
    else:
        form = UploadFileForm()
    return render_to_response('files/home.html',
        locals(),
        context_instance=RequestContext(request)
    )