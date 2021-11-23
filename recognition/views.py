from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Animal, Photo
from .utils import recognize_animal


def index(request):
    if request.method == 'GET':
        return render(request, 'recognition/upload.html')
    new_photo = Photo(img=request.FILES['pht'])
    new_photo.save()
    return redirect(reverse('recognize', kwargs={'photo_id': new_photo.id}))


def recognize(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    slug = recognize_animal(path=photo.img.url)
    animal = Animal.objects.filter(slug=slug).first()
    print(photo.img.url)
    return render(request, 'recognition/result.html', context={'animal': animal.name, 'photo': photo.img.url})
