from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, ListView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from .forms import MenuCreateForm, MenuCreate
from .models import Menu
from .models import MenuCreateModel
from home.utils import find
from menuResponse.utils import encode
import json,urllib.request
from .utils import  load_url
import concurrent.futures
import urllib.parse

# Vista MenuListView
# Descripción: Muestra las opciones de menu creadas para un dia en especifico, permite crear y enviar el menu a slack
# Parametros: UUID del menu
class MenuListView(ListView):
	template_name = 'menu/menu_list.html'
	queryset = Menu.objects.all()	

	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		querysetMenuCreate = MenuCreateModel.objects.all()		
		context['menuCreate'] = querysetMenuCreate
		context['menuCreateId'] = '0'
		return context

	def post(self, request, *args, **kwargs):
		menuCreateId = request.POST.get('selectMenuCreate')
		querysetMenuCreate = MenuCreateModel.objects.all()		
		queryset = Menu.objects.filter(MenuID=menuCreateId)
		context = {
			"object_list" : queryset,
			"menuCreate" : querysetMenuCreate,
			"menuCreateId" : menuCreateId
		}
		return render(request, self.template_name, context)	

# Vista SendToSlack
# Descripción: Obtiene la lista de usuarios de slack y asincronamente enviama reminder a las 11:00 AM
# Parametros: UUID del menu
class SendToSlack(View):
	def get(self,request,*args,**kwargs):
		userList = []
		slackList = []
		# Se obtiene lista de usuario de slack y se crea diccionario id:username
		response = json.load(urllib.request.urlopen("https://slack.com/api/users.list?token="+settings.SLACK_TOKEN+"&pretty=1"))		
		d= {}
		for x in response['members']:
			if (x['id'] != 'USLACKBOT'):
				userList.append(x['id'])
				d[x['id']] = x['name']
		
		# Se crea lista con urls de peticiones get para reminders
		for k in d:						
			if k != 'USLACKBOT':
				personalizedUrl = 'http://127.0.0.1:8000/menuResponse/menu/'+self.kwargs['id']+'/' + encode('test',d[k])				
				slackList.append('https://slack.com/api/reminders.add?token='+settings.SLACK_TOKEN+'&text='+urllib.parse.quote('Recuerda pedir tu menu del dia en ', safe='')+personalizedUrl+'&time='+urllib.parse.quote('11:00 AM', safe='')+'&user=' + k + '&pretty=1')		
		
		# Se inicia proceso asincrono para peticiones usando concurrent.futures
		if (slackList):			
			resp_ok = 0
			with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

				future_to_url = {executor.submit(load_url, url, 10): url for url in     slackList}
				for future in concurrent.futures.as_completed(future_to_url):
					url = future_to_url[future]
					try:
						data = future.result()
					except Exception as exc:
						print(exc)						
					else:
						resp_ok = resp_ok + 1
				print(resp_ok)		
		return HttpResponseRedirect("/menulist")

# Vista MenuUpdateView
# Descripción: Permite actualizar las opciones de menu
# Parametros: ID de la opcion de menu
class MenuUpdateView(UpdateView):
	model = Menu
	fields = ['option','description']
	success_url = reverse_lazy('menulist')

# Vista MenuDelete
# Descripción: Permite eliminar las opciones de menu
# Parametros: ID de la opcion de menu
class MenuDelete(DeleteView):
	model = Menu
	template_name = 'menu/menu_list.html'
	success_url = reverse_lazy('menulist')

# Vista MenuCreateView
# Descripción: Permite crear  opciones de menu
# Parametros: UUID del menu
class MenuCreateView(CreateView):
	form_class = MenuCreate
	model = Menu	
	def dispatch(self, request, *args, **kwargs):
		self.mid = request.POST.get('menuCreateId')
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		context['menuCreateId'] = self.mid
		return context
	# Se hace overright sobre el metodo form_valid para incluir la clave foranea del modelo MENUID = UUID
	def form_valid(self, form):		
		menu = form.save(commit=False)
		menu.MenuID = MenuCreateModel.objects.get(id=self.mid)
		return super(MenuCreateView, self).form_valid(form)
	template_name = 'menu/menu_form.html'
	success_url = reverse_lazy('menulist')


