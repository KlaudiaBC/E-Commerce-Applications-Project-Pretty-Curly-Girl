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
    """
    Custom the 404 Error Page
    """
    return render(request, '404.html')


def handler500(request):
    """
    Custom the 500 Error Page
    """
    return render(request, '500.html')
