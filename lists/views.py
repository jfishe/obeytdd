from django.http import HttpResponse
from django.shortcuts import render

from lists.models import Item

# Create your views here.
def home_page(request):
    """home_page

    Todo
    ----
    * Don't save blank items for every request.
    * Code smell: POST test is too long?
    * Display multiple items in the table.
    * Support more than one list!

    Parameters
    ----------
    request

    Returns
        Return is....

    """
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()

    return render(request, 'home.html',
                  {'new_item_text': request.POST.get('item_text', ''),
                  })
