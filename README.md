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
- Investigacion



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



## Investigacion:

- Inyecciones SQL:

Que son las inyecciones SQL. La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios.



- Cross-Site Scripting (XSS): 

    El Cross-Site Scripting  se trata de un tipo de ataque que aprovecha fallas de seguridad en sitios web y que permite a los atacantes implantar scripts maliciosos en un sitio web legítimo (también víctima del atacante) para ejecutar un script en el navegador de un usuario desprevenido que visita dicho sitio y afectarlo, ya sea robando credenciales, redirigiendo al usuario a otro sitio malicioso

        un ejemplo seria este: https://sitio-inseguro.com/buscar?term=<script>/*Codigo Malicioso*/</script> lo cual es un link que ya viene mailicioso lo que hace que si un usuario entra en ese link empieza el ataque 



- ¿Qué es un ataque CSRF?

Un ataque CSRF ocurre cuando un atacante engaña a un usuario autenticado para que ejecute acciones no deseadas en una aplicación web sin su consentimiento. Esto es posible porque el navegador envía automáticamente las cookies de sesión con cada solicitud.

Frameworks:
Django: Incluye protección CSRF por defecto con el middleware CsrfViewMiddleware, y solo requiere añadir {% csrf_token %} en los formularios.
Express.js: Necesita el middleware csurf, que añade protección CSRF generando y validando tokens en cada solicitud.