from django.shortcuts import render
from django.views import View

# Create your views here.
class AboutView(View):
	template_name = 'about.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})