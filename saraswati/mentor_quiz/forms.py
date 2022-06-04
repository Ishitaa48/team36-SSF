from django import forms
from .models import NineTen, Inter

class NineTenform(forms.ModelForm):
    class Meta:
        model=NineTen
        fields=['Question','op1','op2','op3','op4','ans','subject','Taxonomy']

class Interform(forms.ModelForm):
    class Meta:
        model=Inter
        fields=['Questions','opt1','opt2','opt3','opt4','answer','subject','Taxonomy']