from django.urls import path
from . import views

urlpatterns = [
    #Nombre - Funcion llamada - apodo
    path('', views.home, name='home'),
    path('products', views.list_products, name='products'),
    path('categories', views.list_categories, name='categories'),
    

]