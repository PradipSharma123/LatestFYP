from django.shortcuts import render
from . models import Category, Photo


def index(request):

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}

    return render(request, 'gallery.html', context)
