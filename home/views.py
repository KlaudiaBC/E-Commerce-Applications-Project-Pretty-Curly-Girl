from django.shortcuts import render
from django.http import Http404
from polls.models import Poll


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the 'About Us' page """
    return render(request, 'home/about.html')


def privacy(request):
    """ A view to return the 'Privacy Policy' page """
    return render(request, 'home/privacy_policy.html')


def handler404(request, poll_id):
    """ Error Handler 404 - Page Not Found """
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "templates/404.html", {'poll': p})
