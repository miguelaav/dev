from django.shortcuts import render
from django.views import View
from django.views.generic import  ListView
from menuResponse.models import MenuResponseModel
from menu.models import MenuCreateModel


# Vista HomeView
# Descripción: Procesa la vista del Home mostrando el listado de peticiones realizadas al menu del dia
# Parametros: UUID del menu
class HomeView(ListView):
	template_name = 'home/home_list.html'
	queryset = MenuResponseModel.objects.all()	



	# Se modifica el contexto para incorporar el UUID del menu	
	# Se ejecuta consulta de menus creados para llenar selector
	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		querysetMenuCreate = MenuCreateModel.objects.all()		
		context['menuCreate'] = querysetMenuCreate
		context['menuCreateId'] = '0'
		return context
	
	# En submit se ejecuta consulta inner join para obtener los responses de usuarios en el menu
	# del dia en particular
	def post(self, request, *args, **kwargs):		
		menuCreateId = request.POST.get('selectMenuCreate')
		querysetMenuCreate = MenuCreateModel.objects.all()		
		queryset = MenuResponseModel.objects.select_related('option').filter(MenuID=menuCreateId).values('userName','comments','option__description')		
		context = {
			"object_list" : queryset,
			"menuCreate" : querysetMenuCreate,
			"menuCreateId" : menuCreateId
		}
		return render(request, self.template_name, context)	
	


