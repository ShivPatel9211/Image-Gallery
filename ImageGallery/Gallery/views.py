from django.shortcuts import render,get_object_or_404 , redirect
from .models import Categorise,Photo
from django.core.paginator import Paginator ,EmptyPage , PageNotAnInteger
from django.core.files.base import ContentFile
from PIL import Image 
import numpy as np
# Create your views here.

def gallery(request):
    category = Categorise.objects.all()
    photo = Photo.objects.all()
    allphoto = Paginator(photo,8)
    page=request.GET.get("page")
    try:
        photo=allphoto.page(page)
    except PageNotAnInteger:
        photo=allphoto.page(1)
    except EmptyPage:
        photo=allphoto.page(allphoto.num_pages)

    context ={
        'category':category,
        'photo':photo,
    }
    return render(request,'gallery.html', context)

def viewPhoto(request,id):
    photo = Photo.objects.filter(id =id).first()
    context ={
        'photo':photo,
    }
    return render(request,'view.html',context)

def uploadPhoto(request):
    category = Categorise.objects.all()
    context ={
        'category':category,
    }
    if request.method=="POST":
        caty= request.POST['caty']
        newcaty= request.POST['newcaty']
        image= request.FILES['image']

        if caty =='none':
            caty = Categorise.objects.create(name=newcaty)
        category = get_object_or_404(Categorise, name=caty)
        photo = Photo.objects.create(category=category,image =image)
        return redirect('gallery')

    return render(request,'add.html',context)


def category(request,id):
    category =Categorise.objects.all()
    photo= Photo.objects.filter(category=id)
    
    allphoto = Paginator(photo,8)
    page=request.GET.get("page")
    try:
        photo=allphoto.page(page)
    except PageNotAnInteger:
        photo=allphoto.page(1)
    except EmptyPage:
        photo= allphoto.page(allphoto.num_pages)
    context = {
        'photo':photo,
        'category':category,
     }
    return render(request, 'category.html',context)

def rotateright(request ,id):
    photo = Photo.objects.get(pk=id)
    image = np.array(Image.open(photo.image.file))
    image = Image.fromarray(np.rot90(image, 3))
    image.save(photo.image.file.name)
    return redirect('gallery')

def rotateleft(request,id):
    photo = Photo.objects.get(pk=id)
    image = np.array(Image.open(photo.image.file))
    image = Image.fromarray(np.rot90(image))
    image.save(photo.image.file.name)
    return redirect('gallery')