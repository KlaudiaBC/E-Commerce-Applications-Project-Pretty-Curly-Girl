from django.shortcuts import render


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
    return render(request, "home/404.html")


def handler500(request):
    """ Error Handler 500 - Server Error """
    return render(request, 'home/500.html')
