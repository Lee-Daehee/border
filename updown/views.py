from django.shortcuts import render, redirect, HttpResponse
from mainApp import settings
import os
# Create your views here.

def index(request):
        dirList = os.listdir(settings.MEDIA_ROOT)
        print(dirList)
        context = {"dirList" : dirList }
        return render(request, 'updown/index.html', context)

def upload(request):
    if request.method=="POST":
        for x in request.FILES.getlist("files"):
            upLoadFile = open(settings.MEDIA_ROOT+"\\"+str(x), 'wb')
            for chunk in x.chunks():
                print(chunk)
                upLoadFile.write(chunk)
        
        return redirect("UD:I")
    elif request.method=="GET":
        return render(request, 'updown/upload.html')

def download(request, border_id, fileName):
    path = str(border_id)+"\\"+fileName
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists(file_path):
        readFile = open(file_path, 'rb')
        response = HttpResponse(readFile.read())
        response['Content-Disposition'] = 'attachment; filename'+os.path.basename(file_path)
        na = os.path.splitext(file_path)[1]
        print(na) # .png .jpg
        if na == '.png' or na == '.jpg':
            response['Content-type']='image/png'
        elif na == '.txt':
            response['Content-type']='text/plain'
        elif na == '.xlsx':
            response['Content-type']='application/vnd.ms.excel'
        else :
            return redirect('mainIndex')
        return (response)

def delete(request, border_id, fileName):
    path = str(border_id) +"\\" + fileName
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    os.remove(file_path)

    return redirect('BD:U', border_id)