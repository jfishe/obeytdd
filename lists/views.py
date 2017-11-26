from django.shortcuts import redirect, render

from lists.models import Item

# Create your views here.
def home_page(request):
    """home_page

    Todo
    ----
    * Display multiple items in the table.
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

    return render(request, 'home.html')
