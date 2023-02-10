from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.
#def home(request):


def profiles(request):
#def home(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})

def details(request, pk):
   pk = int(pk)
   item = get_object_or_404(Profile, pk=pk)
   form = ProfileForm(data=request.POST or None, instance=item)
   if request.method == 'POST':
      if form.is_valid():
         form2 = form.save(commit=False)
         form2.save()
         return redirect('profiles')
      else:
         print(form.errors)
   else:
      return render(request, 'profiles/present_profile.html', {'form': form})