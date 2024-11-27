Sistema de gestión de tareas

Este proyecto es una aplicación web para la gestión de tareas personales, diseñada para que cada usuario pueda organizar sus actividades de manera sencilla y eficiente.

Características principales:

Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y gestionar sus propias tareas de forma individual.

Gestión de tareas:
Agregar nuevas tareas con un nombre y una hora opcional.
Marcar tareas como completadas mediante un checkbox.
Editar tareas existentes.
Eliminar tareas cuando ya no sean necesarias.

Interfaz intuitiva:
Las tareas se muestran como tarjetas organizadas verticalmente, ordenados ascendentemente.
Cada tarjeta incluye un checkbox, el nombre y la hora de la tarea, además de botones para editar y eliminar.
Asociación entre usuarios y tareas: Cada tarea está vinculada a un usuario mediante una relación de base de datos, garantizando la privacidad y exclusividad de los datos.

Tecnologías utilizadas:
Frontend: HTML, CSS (diseño puro sin frameworks adicionales).
Backend: Python (Flask) para gestionar rutas, lógica de negocio y conexión con la base de datos.
Base de datos: MySQL, con tablas relacionadas (usuarios y tareas) para manejar la información de usuarios y tareas.
SQL: Uso de consultas SQL parametrizadas para prevenir inyecciones SQL y mejorar la seguridad.

Cómo funciona:
Inicio de sesión y registro:

Los usuarios deben registrarse con un correo electrónico y contraseña para acceder a la aplicación.
Cada vez que un usuario inicia sesión, solo puede ver y gestionar sus propias tareas.
Gestión de tareas:

Los usuarios pueden agregar tareas desde el frontend, especificando un nombre y, opcionalmente, una hora.
Las tareas aparecen ordenadas por hora y se pueden completar, editar o eliminar según sea necesario.

Seguridad:

Todas las consultas a la base de datos utilizan parámetros para prevenir vulnerabilidades como la inyección SQL.
Las tareas están vinculadas al user_id del usuario autenticado, asegurando que cada usuario solo gestione sus propios datos.

Requisitos para ejecutar el proyecto:

Entorno: Python 3.8+ y MySQL.
Instalar dependencias: Ejecutar pip install -r requirements.txt para instalar Flask y otras dependencias necesarias.

Base de datos:

Crear una base de datos MySQL llamada sistema_usuarios.
Ejecutar los scripts de creación de tablas en el archivo db_setup.sql para generar las tablas usuarios y tareas.
Ejecutar la aplicación: Correr el servidor Flask con python app.py y acceder a la interfaz en http://localhost:5000/index.
