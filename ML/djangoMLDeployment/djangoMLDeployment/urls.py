from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('',include('basicConsepts.urls')),
    path('',include('mlApp.urls')),
    path('admin/', admin.site.urls),
]
