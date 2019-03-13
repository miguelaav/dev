from django.shortcuts import render
from django.views.generic import CreateView, ListView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import MenuCreateModel,MenuResponseModel
from menu.models import Menu
from .forms import MenuResponseForm, MenuResponse
import os
from .utils import encode,decode

# Vista MenuResponseRegister
# Descripción: Permite registrar la respuesta del usuario, seleccionar el menu que desea
# Parametros: UUID del menu
# opcion de menu
# comentario
# nombre de usuario
class MenuResponseRegister(CreateView):
	form_class = MenuResponse
	template_name = 'menuResponse/menuResponse_form.html'

	def dispatch(self, request, *args, **kwargs):
		self.mid = request.POST.get('menuCreateId')
		self.optionid = request.POST.get('optionId')
		self.userName = request.POST.get('userName')
		return super().dispatch(request, *args, **kwargs)

	#Se ingresa en el contexto el valor UUID del menu
	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		context['menuCreateId'] = self.mid
		return context

	def get(self,request,*args,**kwargs):
		#Se obtiene el usuario que responde al link por URL		
		userName = decode('test',self.kwargs['user'])
		#Se consulta las opciones del menu disponible para seleccionar
		querysetMenu = Menu.objects.filter(MenuID=self.kwargs['id'])
		#Se consulta si ya ha respondido a la consulta anteriormente
		querysetMenuResponse = MenuResponseModel.objects.filter(userName=userName).filter(MenuID=self.kwargs['id'])
		#Se adjunta todos los datos al contexto para renderizar informacion en template
		context = {
			"form" : MenuResponse,
			"querysetMenu" : querysetMenu,
			"userName" : userName,
			"menuCreateId" : self.kwargs['id'],
			"querysetMenuResponse" : querysetMenuResponse
		}
		return render(request,'menuResponse/menuResponse_form.html',context)

	# Se hace overright sobre el metodo form_valid para incluir todas las claves foraneas del modelo
	def form_valid(self, form):		
		menuResponse = form.save(commit=False)
		menuResponse.MenuID = MenuCreateModel.objects.get(id=self.mid)
		menuResponse.option = Menu.objects.get(id=self.optionid)
		menuResponse.userName = self.userName
		return super(MenuResponseRegister, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('menuresponsecreate', kwargs={'id': self.kwargs['id'],'user':self.kwargs['user']})


	

