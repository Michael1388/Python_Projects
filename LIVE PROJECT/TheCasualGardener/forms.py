from .import forms
from django.forms import ModelForm
from .models import Basket

class BasketForm(ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'