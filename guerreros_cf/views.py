import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django import forms
from .forms import ContactoForm
from .models import Equipo, Noticia, Staff, Anuncio
from django.core.paginator import Paginator


# ─────────────────────────────────────────
# INICIO
# ─────────────────────────────────────────
def inicio(request):

    imagenes = [f"{i}.jpg" for i in range(1, 190)]

    imagenes_filo = [f"filo{i}.jpg" for i in range(1, 12)]
    imagenes_entreno = [f"filo{i}.jpg" for i in range(12, 27)]

    noticias = Noticia.objects.filter(publicado=True)[:6]

    context = {
        "imagenes": imagenes,
        "imagenes_filo": imagenes_filo,
        "imagenes_entreno": imagenes_entreno,
        "noticias": noticias,
    }

    return render(request, "guerreros_cf/inicio.html", context)
# ─────────────────────────────────────────
# EQUIPOS
# ─────────────────────────────────────────
def equipos_lista(request):
    equipos = Equipo.objects.filter(activo=True).prefetch_related('trofeos')

    equipos_femenil = equipos.filter(division='femenil')
    equipos_juvenil = equipos.filter(division='juvenil')
    equipos_varonil = equipos.filter(division='varonil')

    anuncios_activos = Anuncio.objects.filter(activo=True)

    # El último anuncio (orden=99) se muestra aparte, más pequeño, al final de la página
    anuncio_extra = anuncios_activos.filter(orden=99).first()
    anuncios_activos = anuncios_activos.exclude(pk=anuncio_extra.pk) if anuncio_extra else anuncios_activos

    anuncios_todas = [a for a in anuncios_activos if a.division == 'todas']
    anuncios_femenil = [a for a in anuncios_activos if a.division == 'femenil']
    anuncios_juvenil = [a for a in anuncios_activos if a.division == 'juvenil']
    anuncios_varonil = [a for a in anuncios_activos if a.division == 'varonil']

    context = {
        'equipos_femenil': equipos_femenil,
        'equipos_juvenil': equipos_juvenil,
        'equipos_varonil': equipos_varonil,
        'anuncios_todas': anuncios_todas,
        'anuncios_femenil': anuncios_femenil,
        'anuncios_juvenil': anuncios_juvenil,
        'anuncios_varonil': anuncios_varonil,
        'anuncio_extra': anuncio_extra,
    }

    return render(request, 'guerreros_cf/equipos_lista.html', context)

def equipo_detalle(request, pk):
    equipo = get_object_or_404(
        Equipo,
        pk=pk,
        activo=True
    )

    context = {
        'equipo': equipo,
    }

    return render(request, 'guerreros_cf/equipo_detalle.html', context)


# ─────────────────────────────────────────
# NOTICIAS
# ─────────────────────────────────────────
def noticias_lista(request):
    categoria = request.GET.get('categoria')
    noticias_list = Noticia.objects.filter(publicado=True)

    if categoria:
        noticias_list = noticias_list.filter(categoria=categoria)

    paginator = Paginator(noticias_list, 6)
    page = request.GET.get('page')
    noticias = paginator.get_page(page)

    return render(request, 'guerreros_cf/noticias_lista.html', {
        'noticias': noticias,
        'categoria_actual': categoria,
        'categorias': Noticia.CATEGORIA_CHOICES
    })


def noticia_detalle(request, slug):
    noticia = get_object_or_404(
        Noticia,
        slug=slug,
        publicado=True
    )

    Noticia.objects.filter(pk=noticia.pk).update(vistas=noticia.vistas + 1)

    return render(
        request,
        'guerreros_cf/noticia_detalle.html',
        {'noticia': noticia}
    )


def noticias_categoria(request, categoria):
    noticias = Noticia.objects.filter(
        categoria=categoria,
        publicado=True
    )

    return render(
        request,
        'guerreros_cf/noticias_lista.html',
        {
            'noticias': noticias,
            'categoria_actual': categoria,
            'categorias': Noticia.CATEGORIA_CHOICES
        }
    )


# ─────────────────────────────────────────
# LIGA
# ─────────────────────────────────────────
def liga_info(request):
    staff = Staff.objects.filter(activo=True)

    return render(
        request,
        'guerreros_cf/liga_info.html',
        {'staff': staff}
    )


# ─────────────────────────────────────────
# STAFF
# ─────────────────────────────────────────
def staff_lista(request):
    staff = Staff.objects.filter(activo=True)

    return render(
        request,
        'guerreros_cf/staff_lista.html',
        {'staff': staff}
    )


# ─────────────────────────────────────────
# CONTACTO
# ─────────────────────────────────────────
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Mensaje enviado correctamente"
            )
            return redirect('guerreros:contacto')
    else:
        form = ContactoForm()

    return render(
        request,
        'guerreros_cf/contacto.html',
        {
            'form': form
        }
    )


# ─────────────────────────────────────────
# API
# ─────────────────────────────────────────
def api_noticias(request):
    return JsonResponse({'mensaje': 'API noticias'})


# ─────────────────────────────────────────
# ERROR 404
# ─────────────────────────────────────────
def error_404(request, exception):
    return render(
        request,
        'guerreros_cf/404.html',
        status=404
    )
