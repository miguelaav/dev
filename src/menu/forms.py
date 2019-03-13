from django import forms
from .models import Menu

#Se define los forms para las opciones del menu
class MenuCreateForm(forms.Form):
	option = forms.IntegerField()
	description = forms.CharField(required=True)
	MenuID = forms.UUIDField(required=True)

#Se define los campos que seran renderizados automaticamente por el framework
class MenuCreate(forms.ModelForm):
	class Meta:
		model = Menu
		fields = [
			'option',
			'description'			
		]
