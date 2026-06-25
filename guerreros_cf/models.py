from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


# ─────────────────────────────────────────
#  DIRECTOR DE LA LIGA (biografía)
# ─────────────────────────────────────────
class Staff(models.Model):
    CARGO_CHOICES = [
        ('director',   'Director General'),
        ('tecnico',    'Director Técnico'),
        ('secretaria', 'Secretaria General'),
        ('arbitro',    'Coordinador de Árbitros'),
        ('cancha',     'Encargado de Cancha'),
        ('tesorera',   'Tesorera'),
        ('otro',       'Otro'),
    ]

    nombre   = models.CharField(max_length=150)
    cargo    = models.CharField(max_length=20, choices=CARGO_CHOICES, default='director')

    foto     = models.ImageField(upload_to='staff/', blank=True, null=True)

    bio = models.TextField(
        blank=True,
        help_text='Biografía completa: trayectoria, experiencia, visión de la liga, logros, etc.'
    )

    anios_experiencia = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='Años de experiencia dirigiendo la liga o en el fútbol'
    )

    telefono = models.CharField(max_length=20, blank=True)
    email    = models.EmailField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)

    orden    = models.PositiveSmallIntegerField(default=0)
    activo   = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f'{self.nombre} — {self.get_cargo_display()}'


# 🔥 GALERÍA DE FOTOS DEL DIRECTOR / STAFF
class StaffImagen(models.Model):
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='galeria'
    )
    imagen = models.ImageField(upload_to='staff/galeria/')
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Foto de {self.staff.nombre}'


# ─────────────────────────────────────────
#  EQUIPO
# ─────────────────────────────────────────
class Equipo(models.Model):
    DIVISION_CHOICES = [
        ('femenil', 'Femenil'),
        ('juvenil', 'Juvenil'),
        ('varonil', 'Varonil'),
    ]

    nombre = models.CharField(max_length=100)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)

    logo = models.ImageField(
        upload_to='equipos/logos/',
        blank=True,
        null=True,
        help_text='Logo del equipo / foto del logro principal (ej. equipo levantando el trofeo)'
    )

    color_principal = models.CharField(max_length=7, default='#0d2137')
    color_secundario = models.CharField(max_length=7, default='#4db8e8')

    horario_entreno = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)

    descripcion_logros = models.TextField(
        blank=True,
        help_text='Ej: Campeón Nacional Femenil Libre 2025, Subcampeón Liga Juvenil 2024...'
    )

    anio_logro = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='Año en que se obtuvo el logro (ej. 2025)'
    )

    fecha_logro = models.DateField(
        null=True, blank=True,
        help_text='Fecha exacta del logro (día/mes/año)'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['division', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.get_division_display()})'

    def get_absolute_url(self):
        return reverse('guerreros:equipo_detalle', args=[self.pk])


# ─────────────────────────────────────────
#  NOTICIA
# ─────────────────────────────────────────
class Noticia(models.Model):
    CATEGORIA_CHOICES = [
        ('torneo', 'Torneo'),
        ('resultado', 'Resultados'),
        ('inscripciones', 'Inscripciones'),
        ('academia', 'Academia'),
        ('femenil', 'Femenil'),
        ('infraestructura', 'Infraestructura'),
        ('general', 'General'),
    ]

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='general')

    contenido = models.TextField()
    resumen = models.CharField(max_length=300)

    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)

    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    publicado = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    vistas = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('guerreros:noticia_detalle', args=[self.slug])


# 🔥 GALERÍA DE IMÁGENES PARA NOTICIAS
class NoticiaImagen(models.Model):
    noticia = models.ForeignKey(
        Noticia,
        on_delete=models.CASCADE,
        related_name='galeria'
    )
    imagen = models.ImageField(upload_to='noticias/galeria/')
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Imagen de {self.noticia.titulo}'


# ─────────────────────────────────────────
#  CONTACTO
# ─────────────────────────────────────────
class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# ─────────────────────────────────────────
#  TROFEO
# ─────────────────────────────────────────
class Trofeo(models.Model):
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='trofeos'
    )

    nombre_torneo = models.CharField(max_length=150)
    anio = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['-anio']

    def __str__(self):
        return f'{self.nombre_torneo} ({self.anio}) — {self.equipo.nombre}'


# ─────────────────────────────────────────
#  ANUNCIO / PATROCINADOR
# ─────────────────────────────────────────
class Anuncio(models.Model):
    DIVISION_CHOICES = [
        ('todas', 'Todas las divisiones'),
        ('femenil', 'Femenil'),
        ('juvenil', 'Juvenil'),
        ('varonil', 'Varonil'),
    ]

    nombre_patrocinador = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='anuncios/')
    link = models.URLField(blank=True)

    division = models.CharField(
        max_length=20,
        choices=DIVISION_CHOICES,
        default='todas'
    )

    activo = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['orden', '-id']

    def __str__(self):
        return f'{self.nombre_patrocinador} ({self.get_division_display()})'