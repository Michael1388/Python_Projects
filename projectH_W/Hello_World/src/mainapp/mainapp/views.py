from django.http import HttpResponse
from django.shortcuts import render

"""
def home(request):
   print(request.user)
   return HttpResponse ("<h1>Welcome user!</h1>")
"""

"""
def home(request):
   user =request.user
   return HttpResponse ("<h1>Welcome {}!</h1>".format(user))
"""

"""
def home(request):
   user = request.user
   context = (
      {'user': user}
   )
   return render(request, "home.html", context)
"""

"""
def home(request):
   products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
   context = {
      'products': products}

   return render(request, "home.html", context)
"""

def home(request):
   names = ["Cherry", "Apalonia", "Orwell", "Stephen", "Paul", "Wynona"]
   context = {
      'names': names}

   return render(request, "home.html", context)

"""
def home(request):
   profiles = Profile.objects.all()

   return render(request, 'home.html', {'profiles': profiles})
"""