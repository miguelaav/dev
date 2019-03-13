from django.shortcuts import render
from django.views.generic import CreateView, ListView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import MenuCreateModel
from .forms import MenuCreateForm, MenuCreateFormClass
from faker import Factory
import uuid

# Vista MenuCreateList
# Descripción: Permite listar todos los menus del dia creados
# Parametros: UUID del menu
class MenuCreateList(ListView):
	queryset = MenuCreateModel.objects.all()
	template_name = 'menuCreate/menuCreate_list.html'

# Vista MenuCreateRegister
# Descripción: Permite crear menu para un dia especifico
# Parametros: UUID del menu
class MenuCreateRegister(CreateView):
	form_class = MenuCreateFormClass
	template_name = 'menuCreate/menuCreate_form.html'
	success_url = reverse_lazy('menucreatelist')

# Vista MenuCreateDelete
# Descripción: Permite eliminar todos los menus del dia creados
# Parametros: UUID del menu
class MenuCreateDelete(DeleteView):
	model = MenuCreateModel	
	template_name = 'menuCreate/menuCreate_list.html'
	success_url = reverse_lazy('menucreatelist')

