from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUpload
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dashboard/")
        
    
    form = FileUploadForm()
    return render(request, 'files/upload_file.html', {'form':form})
    
    
def get_dashboard(request):
    queryset = FileUpload.objects.all()
    return render(request, 'files/dashboard.html', {'files':queryset})


def download_file(request, pk):
    instance = get_object_or_404(FileUpload, pk=pk)
    file_path = instance.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response