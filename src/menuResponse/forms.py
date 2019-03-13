from django import forms
from .models import MenuResponseModel

class MenuResponseForm(forms.Form):
	option = forms.IntegerField()
	comments = forms.CharField(required=False)
	MenuID = forms.UUIDField(required=True)
	userName = forms.CharField(required=False)

class MenuResponse(forms.ModelForm):
	class Meta:
		model = MenuResponseModel
		fields = [
			'comments'		
		]
