from django.http import HttpResponse
from visits.models import PageVisit
import pathlib
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):

    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()  # Get all PageVisit objects
    page_queryset = PageVisit.objects.filter(path=request.path)  # Filter by path
    try:
        percent = page_queryset.count() / queryset.count() * 100
    except ZeroDivisionError:
            percent = 0
             
    my_title = "Hello, world!"
    my_context = {
        "page_title": my_title,
        "queryset": queryset,
        "page_queryset": page_queryset,
        "pagevisit_count": page_queryset.count(),
        "percent": percent,
        "total_visits": queryset.count(),
    }
    path = request.path
    print("path", path)
    html_template = "home.html"

    PageVisit.objects.create(path=request.path)  # Log the visit  
    return render(request, html_template, my_context)