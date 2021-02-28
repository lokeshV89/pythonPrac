from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # to pass simple html response use below
    #return HttpResponse("hello world")

    # to pass html templates
    #return render(request,'home.html')

    # to pass html templates with variable
    return render(request,'home.html', {'name':'lokesh'})

def add(request):
    # is method is get
    """ num1 = float(request.GET['num1'])
    num2 = float(request.GET['num2']) """

    # if method is post
    num1 = float(request.POST['num1'])
    num2 = float(request.POST['num2'])
    res = num1+num2

    return render(request,'result.html',{'result':res})

