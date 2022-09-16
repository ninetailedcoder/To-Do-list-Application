from django.urls import path
from app import views

urlpatterns= [
    path('', views.home, name='home'),
    path('done/<int:pk>', views.delete, name ='delete')
]