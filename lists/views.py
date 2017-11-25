from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    """TODO: Docstring for home_page.
    Returns
    -------
    TODO

    """
    return HttpResponse('<html><title>To-Do lists</title></html>')
