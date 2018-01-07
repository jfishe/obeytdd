"""
Django views
"""
from django.shortcuts import redirect, render  # type: ignore

from lists.models import Item, List

# Create your views here.


def home_page(request):
    """home_page

    Todo
    ----
    * Refactor away some duplication in urls.py

    Parameters
    ----------
    request

    Returns
        Return is render of home.html

    """
    return render(request, 'home.html')


def view_list(request, list_id):
    """TODO: Docstring for view_list."""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    """TODO: Docstring for new_list."""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    """TODO: Docstring for add_item."""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
