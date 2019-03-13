from django.db import models
from django.db.models.signals import pre_save, post_save
import uuid
from .utils import unique_slug_generator

from menuCreate.models import MenuCreateModel

# Se definen los modelos de las opciones de menu
# Option = opcion del menu (1,2,3,4,etc)
# description = definicion del menu (Pastel de Choclo)
# MenuID = relacion foranea con el menu del dia (menu del dia 2019-03-15)
# Date = Fecha de la creación del registro
class Menu(models.Model):
	option = models.IntegerField(unique=True)
	description = models.CharField(max_length=100) 
	date = models.DateField(auto_now_add=True, blank=True)
	MenuID= models.ForeignKey(MenuCreateModel, default=uuid.uuid4, on_delete=models.CASCADE)

	@property
	def title(self):
		return self.description
'''
def me_pre_save_receiver(sender, instance, *args,**kwargs):
	print('saving')
	#print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

def me_post_save_receiver(sender, instance, created, *args,**kwargs):
	print('saved')
	#print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()

pre_save.connect(me_pre_save_receiver,sender=Menu)
	
post_save.connect(me_pre_save_receiver,sender=Menu)
'''