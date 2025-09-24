from django.urls import path
from . import views

app_name = 'clientes_app'

urlpatterns = [
    path('', views.index, name='index'),
    
    # URLs para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    
    # URLs para Cliente Corporativo
    path('clientes-corporativos/', views.ClienteCorporativoListView.as_view(), name='cliente-corporativo-list'),
    path('clientes-corporativos/nuevo/', views.ClienteCorporativoCreateView.as_view(), name='cliente-corporativo-create'),
    
    # URLs para Producto
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', views.ProductoCreateView.as_view(), name='producto-create'),
    
    # URL para búsqueda
    path('buscar/', views.buscar_producto, name='buscar-producto'),
]