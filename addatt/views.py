from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.
def homepage(request):
    return render(request, "home.html",{})

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'upload.html')

def upload2(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload2.html', {
        'form': form
    })