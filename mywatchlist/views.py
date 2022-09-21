from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'watchlist': data_watchlist,
        'name': "Wedens Elma Malau",
        'npm': "2106751165",
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def show_html(request):
#     data = MyWatchList.objects.all()
#     return HttpResponse(serializers.serialize("html", data), content_type="application/html")
