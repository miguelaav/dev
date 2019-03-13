from django.db import models

from menu.models import Menu
from menuCreate.models import MenuCreateModel

class MenuResponseModel(models.Model):
	option = models.ForeignKey(Menu, blank=False)
	userName = models.CharField(max_length=50, blank=True )
	MenuID= models.ForeignKey(MenuCreateModel, blank=False, on_delete=models.CASCADE)
	comments = models.CharField(max_length=200) 		
	date = models.DateField(auto_now_add=True, blank=True)
