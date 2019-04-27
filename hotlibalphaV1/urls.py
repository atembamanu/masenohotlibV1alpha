from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from hotlibrary.views.indexviews import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('hotlibrary.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
