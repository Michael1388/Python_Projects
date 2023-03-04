from django.shortcuts import render, get_object_or_404, redirect
from .forms import BasketForm
from .models import Basket
import http.client, urllib.parse
import requests
import json


# Function will render TheCasualGardener home page when requested
def TheCasualGardener_home(request):
    return render(request, 'TheCasualGardener/TheCasualGardener_home.html')

# Function will render create_record html page when requested and present a form for input
def createRecord(request):
   form = BasketForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('../list_basket')
   else:
      print(form.errors)
      form = BasketForm()
   context = {
      'form': form,
   }
   return render(request, 'TheCasualGardener/create_Record.html', context)

# Function will render the garden_basket "list" page when requested and show items

def list(request):
   item = Basket.objects.all()
   content = {'item': item}
   return render(request, 'TheCasualGardener/list_basket.html', content)


# Function will render
def details(request, pk):
   entry = get_object_or_404(Basket, pk=pk)
   content = {'entry': entry}
   return render(request, 'TheCasualGardener/basket_details.html', content)


# Function will render
def edit(request, pk):
    pk = int(pk)
    entry = get_object_or_404(Basket, pk=pk)
    form =BasketForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('list_basket')
    content = {'form': form, 'entry': entry}
    return render(request, 'TheCasualGardener/basket_edit.html', content)

# Function will render delete page
def delete(request, pk):
    pk = int(pk)
    entry = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../list_basket')
    content = {'entry': entry}
    return render(request, 'TheCasualGardener/basket_delete.html', content)
# Function for Quote Garden API
def my_api(request):
    url = 'https://api.stockdata.org/v1/data/quote?symbols=AAPL&api_token=CoYkfhpiZlAIA6h1v7tOCH4fqQfgC0xDJmjtlZGL'
    response = requests.request("GET", url)
    # print(response) # should return "<Response [200]> to the terminal
    jsonResponse = json.loads(response.text)

    api_name = "Apple Inc" # jsonResponse["data"][0]["name"]
    api_data = "AAPL" # jsonResponse["data"][0]["ticker"]
    api_price = "144.57" # jsonResponse["data"][0]["price"]
    api_change = "-0.56" # jsonResponse["data"][0]["day_change"]

    print(api_data)

    content = {"api_name": api_name, "api_info": api_data, "api_price": api_price, "api_change": api_change}
    return render(request, 'TheCasualGardener/tcg_api.html', content)
