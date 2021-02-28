from django.shortcuts import render
from django.http import HttpResponse
from getImage.forms import uploadform
from getImage.models import image

# Create your views here.

def index(request):
    return render(request,'uploadForm.html')

def saveImage(request):
    #return HttpResponse('saved')
    saved = False
    if request.method == "POST":
        UploadData = uploadform(request.POST, request.FILES)
        #return HttpResponse(".......//.")

        if UploadData.is_valid():

            data = image()
            data.fname = UploadData.cleaned_data["fname"]
            data.lname = UploadData.cleaned_data["lname"]
            data.email = UploadData.cleaned_data["email"]
            data.title = UploadData.cleaned_data["title"]
            data.filepath = UploadData.cleaned_data["filepath"]
            data.description = UploadData.cleaned_data["desc"]

            data.save()
            saved = True

    else:
        UploadData = uploadform()

    if saved:
        return HttpResponse("saved successfully")
    else:
        return HttpResponse(UploadData.errors)