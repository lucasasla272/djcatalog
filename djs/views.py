from django.shortcuts import redirect, render, get_object_or_404
from .models import DJ
from django.contrib import messages                     # mensajes flash
from django.contrib.auth.decorators import login_required
from .forms import DJForm
from django.db.models import Q
from django.core.paginator import Paginator

# Campos por los que se permite ordenar (seguridad: nunca pasamos el parámetro del usuario directo a order_by, solo estos)
ORDENES_PERMITIDOS = {
    'nombre': 'nombre',
    'estilo': 'estilo',
    'nacionalidad': 'nacionalidad',
    'debut': 'debut_year',
}

def dj_list(request):
    djs = DJ.objects.all()

    # Leemos los filtros que vienen por GET (pueden no existir -> usamos '')
    q = request.GET.get('q', '').strip()
    estilo = request.GET.get('estilo', '').strip()

    # Búsqueda de texto: nombre O nacionalidad (sin distinguir mayúsculas)
    if q:
        djs = djs.filter(Q(nombre__icontains=q) | Q(nacionalidad__icontains=q))

    # Filtro por estilo exacto (viene del desplegable)
    if estilo:
        djs = djs.filter(estilo=estilo)

    # Lista de estilos únicos para rellenar el desplegable
    estilos = DJ.objects.values_list('estilo', flat=True).distinct().order_by('estilo')

     # Orden: solo campos permitidos, con dirección asc/desc
    order = request.GET.get('order', 'nombre')
    dir_ = request.GET.get('dir', 'asc')

    campo = ORDENES_PERMITIDOS.get(order, 'nombre')   # si no es válido, cae a 'nombre'
    if dir_ == 'desc':
        campo = '-' + campo
    djs = djs.order_by(campo)
    
    paginator = Paginator(djs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'djs/dj_list.html', {
        'page_obj': page_obj, 'q': q, 'estilo': estilo, 'estilos': estilos,
        'order': order, 'dir': dir_, 'ordenes': ORDENES_PERMITIDOS,
    })


def dj_detail(request, pk):
    dj = get_object_or_404(DJ, pk=pk)   # el DJ o error 404
    return render(request, 'djs/dj_detail.html', {'dj': dj})

@login_required
def dj_create(request):
    if request.method == 'POST':
        form = DJForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ {form.cleaned_data["nombre"]} agregado al catálogo.')
            return redirect('djs:dj_list')
        messages.error(request, '❌ Revisá los errores del formulario.')   # validación falló
    else:
        form = DJForm()
    return render(request, 'djs/dj_form.html', {'form': form, 'mode': 'create'})


@login_required
def dj_update(request, pk):
    dj = get_object_or_404(DJ, pk=pk)
    if request.method == 'POST':
        form = DJForm(request.POST, instance=dj)         # rellena con los datos actuales
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ {dj.nombre} actualizado.')
            return redirect('djs:dj_detail', pk=dj.pk)
        messages.error(request, '❌ Revisá los errores del formulario.')
    else:
        form = DJForm(instance=dj)
    return render(request, 'djs/dj_form.html', {'form': form, 'mode': 'update', 'dj': dj})


@login_required
def dj_delete(request, pk):
    dj = get_object_or_404(DJ, pk=pk)
    if request.method == 'POST':
        messages.success(request, f'🗑️ {dj.nombre} eliminado del catálogo.')
        dj.delete()
        return redirect('djs:dj_list')
    return render(request, 'djs/dj_confirm_delete.html', {'dj': dj})