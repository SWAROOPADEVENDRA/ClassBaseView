from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View


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

class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')