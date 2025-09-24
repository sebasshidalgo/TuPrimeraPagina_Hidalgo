from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Cliente, ClienteCorporativo, Producto, Compra
from .forms import ClienteForm, ClienteCorporativoForm, ProductoForm, BusquedaForm

# Vista principal - página de inicio
def index(request):
    return render(request, 'clientes_app/index.html')

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes_app/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes_app/cliente_form.html'
    success_url = reverse_lazy('clientes_app:cliente-list')

# Vistas para ClienteCorporativo
class ClienteCorporativoListView(ListView):
    model = ClienteCorporativo
    template_name = 'clientes_app/cliente_corporativo_list.html'
    context_object_name = 'clientes_corporativos'

class ClienteCorporativoCreateView(CreateView):
    model = ClienteCorporativo
    form_class = ClienteCorporativoForm
    template_name = 'clientes_app/cliente_corporativo_form.html'
    success_url = reverse_lazy('clientes_app:cliente-corporativo-list')

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'clientes_app/producto_list.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'clientes_app/producto_form.html'
    success_url = reverse_lazy('clientes_app:producto-list')

# Vista de búsqueda
def buscar_producto(request):
    productos = []
    form = BusquedaForm()
    
    if request.GET:
        form = BusquedaForm(request.GET)
        if form.is_valid():
            criterio = form.cleaned_data.get('criterio')
            if criterio:
                # Búsqueda en múltiples campos
                productos = Producto.objects.filter(
                    nombre__icontains=criterio
                ) | Producto.objects.filter(
                    descripcion__icontains=criterio
                ) | Producto.objects.filter(
                    codigo_sku__icontains=criterio
                )
    
    return render(request, 'clientes_app/busqueda.html', {
        'form': form,
        'productos': productos
    })

    