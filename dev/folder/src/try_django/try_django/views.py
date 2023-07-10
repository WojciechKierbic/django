from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    context = {"title": "Hello there", "my_list": [1,2,3,4, 5]}
    return render(request, "homepage.html", context)
    
def contact_page(request):
    return render(request, "contact.html", {"title": "Contact"})

def about_page(request):
    return render(request, "about.html", {"title": "About"})

def example_page(request):
    template_obj = get_template("example.html")
    return HttpResponse(template_obj.render({"title": "Example"}))