from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View

from app.forms import *

# string response by using FBV
def stirngByFbv(request):
    return HttpResponse('stirngByFbv is return the response in function base view')

# string response by using CBV
class StringByCbv(View):
    def get(self,request):
        return HttpResponse('StringByCbv is return the response in class base view')

# Html response by using FBV
def htmlByFbv(request):
    return render(request,'htmlByFbv.html')


# Html response by using CBV
class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')

# Insert the data into function base view
def insert_data_fbv(request):
     d={'ESFO':SchoolForm()}
     if request.method=='POST':
         ESDO=SchoolForm(request.POST)
         if ESDO.is_valid():
             ESDO.save()
             return HttpResponse('Insert the data successfully')
         else:
             return HttpResponse('Invalid data')
     return render(request,'insert_data_fbv.html',d)

# Insert the data into class base view
class InsertDataCbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'InsertDataCbv.html',d)
    
    def post(self,request):
        ESDO=SchoolForm(request.POST)
        if ESDO.is_valid():
            ESDO.save()
            return HttpResponse('Insert the data successfully')
        else:
            return HttpResponse('Invalid data')
