# 🎧 Catálogo de DJs

Aplicación web desarrollada con Django como práctica del módulo de Desarrollo Web.

Permite gestionar un catálogo de DJs de música electrónica: listado público con
búsqueda, filtros, orden y paginación, y un CRUD completo protegido por login.

## Funcionalidades

- Listado de DJs **público** con:
  - Búsqueda de texto por nombre o nacionalidad (`?q=`)
  - Filtro por estilo (`?estilo=`)
  - Orden configurable por campos permitidos, ascendente o descendente (`?order=`, `?dir=`)
  - Paginación de 10 en 10 que preserva filtros y orden (`?page=`)
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
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1

## Superuser
Usuario: pyhton
Contraseña: Super2026@