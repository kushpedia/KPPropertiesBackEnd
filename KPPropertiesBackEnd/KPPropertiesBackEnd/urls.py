from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url
from Properties.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',ReactView.as_view(),name="apiview"),
	# path('properties/', include('Properties.urls')),
]
