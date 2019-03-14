from django.shortcuts import render
from django.views.generic import  ListView
from django.contrib.auth.models import User

class CreateUserView(ListView):
	template_name = 'createUserNora/createUserNora_list.html'
	queryset = User.objects.filter(username='nora')
	
	def get(self, request, *args, **kwargs):
		queryset = User.objects.filter(username='nora')
		if (not queryset):			
			user = User.objects.create_user(username='nora', email='nora@cornershop.com',password='1234')
			message = "Usuario 'nora' Creado con la password: 1234"
		else:
			message = "Usuario 'nora' ya existe en la base con la password: 1234"
			
		context = {
			"object_list" : queryset,
			"message": message
		}
			
		return render(request, self.template_name, context)	
	#user = User.objects.create_user(username='nora', email='nora@cornershop.com',password='1234')