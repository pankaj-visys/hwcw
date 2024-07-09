from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, FileResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UploadFileForm
from .models import Myfiles
import os
import datetime

# Create your views here.
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.user)
        time = datetime.datetime.now()
        for file in request.FILES.getlist('file'):
            print(str(file))
            submitterName = request.user
            batchName = str(time) + str(submitterName)
            print(batchName)
            photo = Myfiles.objects.create(fileName=file,submitter=submitterName , batch=batchName)
            photo.save()


        filename = "testfile.pdf"
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        print("filepath")
        print(filepath)
        print("fileresponse")
        print(FileResponse(open(filepath, 'rb'), content_type='application/pdf'))
        return HttpResponse("The name of the file is " + str(file))
    else:
        form = UploadFileForm()

    return render(request, 'administration/upload.html', {'form' : form})


@login_required
def payslip_view(request):
    filename = "testfile.pdf"
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    print("filepath")
    print(filepath)
    print("fileresponse")
    showfile = FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    return render(request, 'administration/showpdf.html', {'pdffile' : showfile})