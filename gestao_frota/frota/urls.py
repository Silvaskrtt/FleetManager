from django.urls import path
from . import views

urlpatterns = [
    # A URL raiz ('') vai chamar a view 'lista_carros'
    path('', views.lista_carros, name='lista_carros'),
    path('adicionar/', views.adicionar_carro, name='adicionar_carro'),
    path('editar/<int:pk>/', views.editar_carro, name='editar_carro'),
    path('excluir/<int:pk>/', views.excluir_carro, name='excluir_carro'),
]
