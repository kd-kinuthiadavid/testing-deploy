from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    return render(request, 'index.html', {"date":date, "images":images})

def painting_images(request):
    date = dt.date.today()
    images = Image.get_painting()
    return render(request, 'painting.html', {"date":date, "images":images})

def image(request, image_id):
    try:
        image = Image.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'image.html', {"image": image})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
