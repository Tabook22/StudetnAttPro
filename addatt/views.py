import csv, io
from django.contrib import messages
from django.contrib.decorators import permission_required
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
    
@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template="contact_upload.html"
    
    prompt={
        'order':'Order of CSV should be first_name, last_name, email,ip_address, message'
    }
    
    if request.method=="GET":
        return render(request, template, prompt)
    csv_file=request.FILES('file') #grab the file from the file system
    
    #check to see if it is csv file
    
    if not csv.file.name.endwith('.csv'):
        message.error(request.'this is not a csv file')
    
    data_set=csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string) #skip the first line because it will contain the headers
    
    for column in csv.reader(io.string, delimiter=',', quotechar="|"):
        _, created=Contact.objects.update_or_crate(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            ip_address=column[3],
            message=column[4]
        )
        
    context={}
    
    return render(request,template, context)