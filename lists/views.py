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
    * Adjust model so that items are associated with different lists.
    * Add unique URLs for each list.
    * Add URLs for adding a new item to an existing list via POST.

    Parameters
    ----------
    request

    Returns
        Return is render of home.html

    """
    return render(request, 'home.html')


def view_list(request):
    """TODO: Docstring for view_list."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """TODO: Docstring for new_list."""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
