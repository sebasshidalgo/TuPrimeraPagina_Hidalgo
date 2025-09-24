# TuPrimeraPagina - Hidalgo

Este proyecto es un **Sistema de Gestión de Clientes y Productos** desarrollado con **Django** para el curso de **Python** de **CoderHouse**.


📋 Descripción

Sistema básico de gestión que permite:

. Registrar clientes
. Registrar clientes corporativos vinculados a un representante legal
. Gestionar productos
. Buscar productos por nombre, descripción o código SKU

🖥️ Cómo usar el sistema

. Página principal: Información general del sistema

. Clientes: Ver lista de clientes y crear nuevos

. Clientes Corporativos: Ver y crear clientes empresariales

. Productos: Ver catálogo y crear nuevos productos

. Búsqueda: Buscar productos en la base de datos

🗄️ Base de datos

. La base de datos SQLite incluye información precargada para probar las funciones del sitio

📦 Modelos del sistema

. Cliente: Datos personales de clientes

. ClienteCorporativo: Información de empresas relacionadas con un cliente

. Producto: Catálogo de productos con stock y precios

. Compra: Registro de transacciones entre clientes y productos


🏗️ Estructura del proyecto

El sistema sigue el patrón MVT (Modelo - Vista - Template) de Django:

. Templates con herencia HTML

. Vistas basadas en clases

. Formularios para todos los modelos

🗂️ Árbol de archivos
```
TuPrimeraPagina_Hidalgo/
│
├── manage.py                     # Script de administración de Django
│
├── TuPrimeraPagina_Hidalgo/      # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py               # Configuración general
│   ├── urls.py                   # URLs principales
│   ├── asgi.py
│   └── wsgi.py                   # Configuración para despliegue
│
├── clientes_app/                 # Aplicación principal
│   ├── __init__.py
│   ├── admin.py                  # Configuración del panel de administración
│   ├── apps.py
│   ├── forms.py                  # Formularios para modelos
│   ├── models.py                 # Modelos de datos (Cliente, ClienteCorporativo, Producto, Compra)
│   ├── tests.py
│   ├── urls.py                   # URLs de la aplicación
│   ├── views.py                  # Vistas y lógica de negocio
│   ├── logic/                    # Lógica adicional
│   │   └── utils.py              # Utilidades
│   └── migrations/               # Migraciones de la base de datos
│       └── __init__.py
│
├── templates/                    # Plantillas HTML
│   ├── base.html                 # Plantilla base con herencia
│   └── clientes_app/             # Plantillas específicas
│       ├── index.html            # Página de inicio
│       ├── cliente_list.html     # Lista de clientes
│       ├── cliente_form.html     # Formulario para crear/editar clientes
│       ├── cliente_corporativo_list.html
│       ├── cliente_corporativo_form.html
│       ├── producto_list.html
│       ├── producto_form.html
│       └── busqueda.html         # Formulario de búsqueda
│
└── db.sqlite3                    # Base de datos SQLite con datos precargados
```

👨🏻‍💻 Developer

Sebastián Matías Hidalgo
Curso de Python - CoderHouse 2025
