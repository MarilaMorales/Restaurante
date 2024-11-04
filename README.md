## Nombre del Proyecto: Laboratorio API

## API de Gestión de Restaurantes


- Esta es una API creada con Django REST Framework que permite gestionar varios aspectos relacionados con un restaurante, incluyendo usuarios, productos, menús, órdenes y más. Ofrece funcionalidades para crear, leer, actualizar y eliminar recursos, mediante un CRUD.

## Índice
- Tecnologías utilizadas
- Herramientas de Testeo
- Características
- Descripción de Archivos
- Endpoints
- Esquema



## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MYSQL



## Herramienta de Testeo

- POSTMAN




## Características

- Crear, leer, actualizar y eliminar reseñas, menús, pagos, empleados, proveedores, productos, promociones, administradores, direcciones, categorías, restaurantes y usuarios.

- Filtrar órdenes por estado.

- Autenticación mediante JWT.



## Descripción de Archivos


- models.py: Define los modelos de datos utilizados en la API.

- serializers.py: Contiene los serializers para validar y transformar los datos.

- views.py: Implementa la lógica de negocio y las vistas de la API.

- urls.py: Configura las rutas y endpoints de la API.

- settings.py: Configura la aplicación Django, incluyendo la base de datos y middleware.




## Endpoints

La API ofrece los siguientes endpoints:

GET : Obtiene todas las datos registrados.
GET /¿?/:id: Obtiene un  dato en específico dependiendo del ID.
POST /¿?/: Crea un nuevo dato.
PUT /¿?/:id: Actualiza un dato existente mediante el ID especifico.
DELETE /¿?/:id: Elimina un dato en especifico por medio del ID.





## Esquema

/RESTAURANTE/
│
├── Restaurante/
│   ├── api/
│   └──── migrations/
│      ├── models.py
│      ├── serializers.py
│      ├── views.py
│      └── urls.py
│
├── Restaurante/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
│
└── README.md