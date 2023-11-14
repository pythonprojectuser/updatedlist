from django import forms
from .models import Carlist
class CarlistForm(forms.ModelForm):
    class Meta:
        model=Carlist
        fields=['name','desc','year','img']