from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify

from .models import Foto, Categoria
from .forms import FotografiaForm, CategoriaForm


# ==========================================
# VISTAS PÚBLICAS
# ==========================================

def home(request):
    categoria_slug = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    
    if categoria_slug:
        fotos = Foto.objects.filter(categoria__slug=categoria_slug)
    else:
        fotos = Foto.objects.all()
        
    context = {
        'categorias': categorias,
        'fotos': fotos,
        'cat_activa': categoria_slug
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def galeria(request):
    fotos = Foto.objects.all()
    return render(request, 'core/galeria.html', {'fotos': fotos})


# ==========================================
# PANEL DE CONTROL / DASHBOARD (CRUD)
# ==========================================

@login_required
def dashboard(request):
    fotos = Foto.objects.all()
    categorias = Categoria.objects.all()
    
    return render(request, 'core/dashboard.html', {
        'fotos': fotos, 
        'categorias': categorias,
    })


@login_required
def crear_foto(request):
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografía agregada con éxito.')
            return redirect('dashboard')
    else:
        form = FotografiaForm()
    return render(request, 'core/foto_form.html', {'form': form, 'titulo_vista': 'Agregar Nueva Fotografía'})


@login_required
def editar_foto(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografía actualizada correctamente.')
            return redirect('dashboard')
    else:
        form = FotografiaForm(instance=foto)
    return render(request, 'core/foto_form.html', {'form': form, 'titulo_vista': 'Editar Fotografía'})


@login_required
def eliminar_foto(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    if request.method == 'POST':
        foto.delete()
        messages.success(request, 'Fotografía eliminada.')
        return redirect('dashboard')
    return render(request, 'core/foto_confirm_delete.html', {'foto': foto})


@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('galeria')  # Redirige a la galería u otra vista
    else:
        form = CategoriaForm()
    
    return render(request, 'core/crear_categoria.html', {'form': form})


@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        nombre = categoria.nombre
        categoria.delete()
        messages.success(request, f'La categoría "{nombre}" ha sido eliminada.')
        return redirect('dashboard')
    return render(request, 'core/eliminar_categoria.html', {'categoria': categoria})