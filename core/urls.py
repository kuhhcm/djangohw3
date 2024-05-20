from django.contrib import admin
from django.urls import path
from app.views import home, about, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
