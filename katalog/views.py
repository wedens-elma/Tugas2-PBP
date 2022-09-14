from django.shortcuts import render

# TODO: Create your views here.

from katalog.models import CatalogItem
def show_katalog(request):
    return render(request, "katalog.html", context)

data_item_katalog = CatalogItem.objects.all()
context = {
    'list_item': data_item_katalog,
    'name': 'Wedens Elma Malau',
    'npm' : '2106751165'
}
