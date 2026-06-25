from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Staff,
    StaffImagen,
    Equipo,
    Noticia,
    Contacto,
    Trofeo,
    Anuncio
)


# ─────────────────────────
# STAFF / DIRECTOR DE LA LIGA
# ─────────────────────────
class StaffImagenInline(admin.TabularInline):
    model = StaffImagen
    extra = 1


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'anios_experiencia', 'activo', 'vista_previa')
    list_filter = ('cargo', 'activo')
    search_fields = ('nombre',)
    inlines = [StaffImagenInline]

    def vista_previa(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:50%;" />',
                obj.foto.url
            )
        return '—'
    vista_previa.short_description = 'Foto'


# ─────────────────────────
# TROFEO (inline en Equipo)
# ─────────────────────────
class TrofeoInline(admin.TabularInline):
    model = Trofeo
    extra = 1


# ─────────────────────────
# EQUIPO
# ─────────────────────────
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'division', 'activo')
    list_filter = ('division', 'activo')
    search_fields = ('nombre',)
    inlines = [TrofeoInline]


# ─────────────────────────
# NOTICIA
# ─────────────────────────
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'publicado')
    list_filter = ('categoria', 'publicado')
    search_fields = ('titulo',)


# ─────────────────────────
# CONTACTO
# ─────────────────────────
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha')
    search_fields = ('nombre', 'email')


# ─────────────────────────
# ANUNCIO / PATROCINADOR
# ─────────────────────────
@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('nombre_patrocinador', 'division', 'orden', 'activo', 'vista_previa')
    list_filter = ('division', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('nombre_patrocinador',)

    def vista_previa(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:4px;" />',
                obj.imagen.url
            )
        return '—'
    vista_previa.short_description = 'Vista previa'
