"""masenohotlibV1alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from msuhotlib.views import HomeView, LoginView, AndroidView, UploadView, UploadpastView, ResourceView, AboutView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(),),
    url(r'^about', AboutView.as_view(),),
    url(r'^upload', UploadView.as_view(),), 
    url(r'^past_upload', UploadpastView.as_view(),), 
    url(r'^resource_upload', ResourceView.as_view(),), 
    url(r'^android', AndroidView.as_view(),),
    url(r'^contact', ContactView.as_view(),),
    url(r'^login', LoginView.as_view(),),

]


# if settings.DEBUG:
# 	urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 	urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)