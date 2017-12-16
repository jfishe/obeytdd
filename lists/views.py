from django.shortcuts import redirect, render

from lists.models import Item

# Create your views here.
def home_page(request):
    """home_page

    Todo
    ----
    * Support more than one list!

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
