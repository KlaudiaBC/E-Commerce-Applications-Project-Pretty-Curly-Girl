from django.shortcuts import render
from django.http import Http404


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the 'About Us' page """
    return render(request, 'home/about.html')


def privacy(request):
    """ A view to return the 'Privacy Policy' page """
    return render(request, 'home/privacy_policy.html')


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    raise Http404("Page does not exist")
    return render(request, "templates/404.html")
