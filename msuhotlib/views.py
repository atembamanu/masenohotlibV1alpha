from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'index.html'

class UploadView(TemplateView):
	template_name = 'upload.html'
class UploadpastView(TemplateView):
	template_name = 'upload_past.html'
class ResourceView(TemplateView):
	template_name = 'upload_resource.html'
class LoginView(TemplateView):
	template_name = 'login.html'
class AndroidView(TemplateView):
	template_name = 'android.html'
class AboutView(TemplateView):
	template_name = 'about_us.html'
class ContactView(TemplateView):
	template_name = 'contact.html'
