from django.shortcuts import redirect, render

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
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
