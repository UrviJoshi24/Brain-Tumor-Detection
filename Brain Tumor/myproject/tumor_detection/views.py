from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'tumor_detection/index.html')
