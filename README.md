# 🎧 Catálogo de DJs

Aplicación web desarrollada con Django como práctica del módulo de Desarrollo Web.

Permite gestionar un catálogo de DJs de música electrónica: listado público con búsqueda, filtros, orden y paginación, y un CRUD completo protegido por login.

## Funcionalidades

- Listado de DJs **público** con:
    - Búsqueda de texto por nombre o nacionalidad (?q=)
    - Filtro por estilo (?estilo=)
    - Orden configurable por campos permitidos, ascendente o descendente (?order=, ?dir=)
    - Paginación de 10 en 10 que preserva filtros y orden (?page=)
- Detalle de cada DJ (público)
- Agregar, editar y eliminar DJs (**solo usuarios autenticados**, con mensajes de éxito/error)
- Login y logout con las vistas genéricas de Django
- Validación personalizada: el año de debut no puede ser futuro
- Panel de administración configurado (búsqueda y filtros)

## Tecnologías

- Python 3
- Django
- SQLite
- HTML + CSS

## Cómo ejecutar el proyecto

1. Clonar o descargar el proyecto y abrir la carpeta en la terminal
2. Crear y activar el entorno virtual:

    python -m venv .venv
    .venv\Scripts\Activate.ps1

3. Instalar dependencias:

    pip install -r requirements.txt

4. Aplicar migraciones:

    python manage.py migrate

5. Levantar el servidor (la base de datos de prueba ya está incluida):

    python manage.py runserver

6. Abrir http://127.0.0.1:8000/

## Usuario de prueba

- Usuario: python
- Contraseña: Super2026@

Si se crea la base de datos desde cero, generar el superusuario con: python manage.py createsuperuser

## Ejemplos de URLs con parámetros

- Búsqueda: http://127.0.0.1:8000/?q=carl
- Filtro por estilo: http://127.0.0.1:8000/?estilo=Techno
- Orden descendente por año de debut: http://127.0.0.1:8000/?order=debut&dir=desc
- Combinación completa: http://127.0.0.1:8000/?estilo=Deep+House&order=debut&dir=asc&page=1
- Detalle de un DJ: http://127.0.0.1:8000/1/

## Notas

- El listado y el detalle son públicos; crear, editar y eliminar requieren iniciar sesión.
- Los datos iniciales (11 DJs) ya están cargados en la base de datos incluida.
- El panel de administración está en /admin/.