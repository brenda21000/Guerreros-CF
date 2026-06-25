# ⚽ Academia Crística Guerreros CF — Proyecto Django

Sitio web completo para la Academia Crística Guerreros CF,
Yauhquemehcan, Tlaxcala, México.

---

## 📁 Estructura del Proyecto

```
guerreros_proyecto/
├── manage.py
├── requirements.txt
├── README.md
│
├── guerreros_proyecto/          ← Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── guerreros_cf/               ← App principal
    ├── models.py               ← Modelos de base de datos
    ├── views.py                ← Vistas / lógica
    ├── urls.py                 ← Rutas de la app
    ├── admin.py                ← Panel de administración
    ├── forms.py                ← Formularios
    ├── apps.py
    │
    ├── templates/
    │   └── guerreros_cf/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── equipos_lista.html
    │       ├── noticias_lista.html
    │       ├── contacto.html
    │       └── ...
    │
    └── static/
        └── guerreros_cf/
            ├── css/main.css
            ├── js/main.js
            └── img/
```

---

## 🚀 Instalación y Configuración

### 1. Clonar / abrir en VS Code
Abre la carpeta `guerreros_proyecto` en Visual Studio Code.

### 2. Crear entorno virtual
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (para el admin)
```bash
python manage.py createsuperuser
```
Sigue las instrucciones: usuario, correo y contraseña.

### 6. Recolectar archivos estáticos (opcional en dev)
```bash
python manage.py collectstatic
```

### 7. Correr el servidor de desarrollo
```bash
python manage.py runserver
```

Abre en tu navegador: **http://127.0.0.1:8000**

Panel de administración: **http://127.0.0.1:8000/admin**

---

## 🗺️ URLs del Sistema

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | `inicio` | Página principal |
| `/equipos/` | `equipos_lista` | Lista de equipos |
| `/equipos/<id>/` | `equipo_detalle` | Detalle de equipo |
| `/jugadores/` | `jugadores_lista` | Directorio de jugadores |
| `/jugadores/<id>/` | `jugador_perfil` | Perfil de jugador |
| `/noticias/` | `noticias_lista` | Noticias paginadas |
| `/noticias/<slug>/` | `noticia_detalle` | Noticia completa |
| `/liga/` | `liga_info` | Info de la liga |
| `/liga/tabla/` | `tabla_posiciones` | Posiciones |
| `/liga/resultados/` | `resultados` | Resultados |
| `/liga/calendario/` | `calendario` | Próximos partidos |
| `/directiva/` | `staff_lista` | Directiva |
| `/inscripciones/` | `inscripcion_nueva` | Formulario inscripción |
| `/contacto/` | `contacto` | Formulario contacto |
| `/admin/` | Django Admin | Panel admin |
| `/api/tabla/` | `api_tabla` | API JSON tabla |
| `/api/noticias/` | `api_noticias` | API JSON noticias |
| `/api/partidos/` | `api_partidos` | API JSON partidos |

---

## 🗄️ Modelos

- **Staff** — Directiva y cuerpo técnico
- **Equipo** — 3 divisiones (Femenil, Juvenil, Varonil)
- **Jugador** — Registro y estadísticas por jugador
- **Partido** — Resultados y calendario
- **Noticia** — Blog/noticias con categorías
- **Inscripcion** — Solicitudes de ingreso
- **Contacto** — Mensajes del formulario

---

## ⚙️ Extensiones recomendadas para VS Code

- **Python** (Microsoft)
- **Django** (Baptiste Darthenay)
- **Pylance**
- **SQLite Viewer** (para ver db.sqlite3)
- **Django Template Linter**

---

## 📍 Cancha / Sede

**EMSAD Yauhquemehcan**
Tlaxcala, México
Coordenadas: 19.4106° N, 98.1849° W
[Ver en Google Maps](https://www.google.com/maps/search/EMSAD+Yauhquemehcan/@19.410603,-98.184883,17z)

---

*Academia Crística Guerreros CF — Pasión por el fútbol ⚽ · Desde 2019*
