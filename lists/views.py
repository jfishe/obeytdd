"""
Django views
"""
from django.shortcuts import redirect, render  # type: ignore

from lists.models import Item

# Create your views here.


def home_page(request):
    """home_page

    Todo
    ----
    * Adjust model so that items are associated with different lists.
    * Add unique URLs for each list.
    * Add a URL for creating a new list via POST.
    * Add URLs for adding a new item to an existing list via POST.

    Parameters
    ----------
    request

    Returns
        Return is....

    """
    return render(request, 'home.html')


def view_list(request):
    """TODO: Docstring for view_list.

    Returns
    -------
    TODO

    """
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """TODO: Docstring for new_list.
    Returns
    -------
    TODO

    """
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
