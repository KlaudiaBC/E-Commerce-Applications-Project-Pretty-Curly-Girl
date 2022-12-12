from django.test import Client


csrf_client = Client(enforce_csrf_checks=True)
