from django import forms
from .models import MenuCreateModel
import os
from django.conf import settings
import datetime

#Se define los forms para el menu del dia
class MenuCreateForm(forms.Form):
	date = forms.DateField(widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                "class": "form-control text-input",
            }
        ),
        input_formats=settings.DATE_INPUT_FORMATS,
        initial=datetime.datetime.today,)
	
#Se define los campos que seran renderizados automaticamente por el framework
# unicamente se selecciona la fecha del menu
class MenuCreateFormClass(forms.ModelForm):
	class Meta:
		model = MenuCreateModel
		fields = [
			'date'
		]
