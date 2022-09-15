from django.shortcuts import render 
from django.http import HttpResponse , jsonResponse
from .models import store

def index(request):
    stores = store.objects.all().values("st_name","st_location","st_Address","st_status","seller"
    "seller_sellname","seller_sell_gender")

    return render(request,"index.html",("store": stores)) 

def search(request):
    return render(request,"search.html")

def search_action(request):
    search_item = request.GET.get("search_item")
    stores = list(store.objects.all().values("st_name","st_location","st_Address","st_status","seller"
    "seller_sellname","seller_sell_gender"))
    return jsonResponse({"store_result": store})

def signup(request):
    return render(request,"signup.html")
# # Create your views here.
# def karan(request):
#     return HttpResponse("<h1>'HI karan'</h1>")