from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import basicsiteinfo,contact
# Create your views here.
def index(request):
  basic = basicsiteinfo.objects.all()
  data = {
    'basicinfo':basic,
  }
  return render(request, 'index.html',data)

def savecontact(request):
  name = request.POST['name']
  email = request.POST['email']
  message = request.POST['message']
  cmt = contact(name=name,email=email,message=message)
  cmt.save()
  #contact.save()
  return HttpResponse('Welcome to from Data <a href="/"> Go Back Home</a> ')
  redirect('/')