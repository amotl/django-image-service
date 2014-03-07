# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from PIL import Image
from StringIO import StringIO
from django.shortcuts import render_to_response, redirect
from django.http import  HttpResponse, HttpResponseNotFound
from image_service.forms import UploadFileForm 
from image_service.mogile import handle_uploaded_file, get_filedata

def upload(request):
    P = request.POST
    if P:
        form = UploadFileForm(P, request.FILES)
        if form.is_valid():
            key = handle_uploaded_file(request.FILES['file'])
            return redirect('/image_service/display/%s' % key)
    else:
        form = UploadFileForm()

    return render_to_response('image_service/upload.html', {"form": form})

def display(request, key=None, demension_x=0, demension_y=0, process=''):
    dx,dy = int(demension_x), int(demension_y)
    file_data = get_filedata(key)
    buf = StringIO()
    buf.write(file_data)
    buf.seek(0)
    image = Image.open(buf)

    if process == 'c':
        image = image.crop((0,0,dx,dy))
    else:
        image = image.resize((dx,dy))

    sio = StringIO()
    image.save(sio,"JPEG")
    sio.seek(0)
    file_data = sio.read()

    if file_data:
        response = HttpResponse(file_data, mimetype="image/jpeg")
    else:
        response = HttpResponseNotFound()
    
    return response
