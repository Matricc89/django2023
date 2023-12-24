# blogPython


```Es un proyecto diseñado tipo blog para que los  Profesores  puedan tener un espacio donde poner algun curso,  Referir algun curso, comentar sobre algun post tanto estudiante como profesor, tiene rol de admin que puede borrar cualquier post o editarlo. Podes subir una foto a tu perfil.```

# Creadores Brian Trias | Matias Ricci  

# Video del proyecto en YouTube

  https://youtu.be/f4sXKyFinuI?si=2LQUaa7ZtPvGHfjY

# Instrucciones para ejecutar este proyecto


1. Crear y activar entorno virtual

   - **Windows:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

   - **Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Instalar las dependencias del proyecto

    ```bash
    pip install -r requirements.txt
    ```

3. Navegar hacia la carpeta del proyecto my_blog

    ```bash
    cd my_blog
    ```

4. Crear las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django

    ```bash
    python manage.py makemigrations
    ```

5. Ejecutar la migración para crear la base de datos con la que trabajará nuestro proyecto de Django

    ```bash
    python manage.py migrate
    ```

6. Crear el superusuario para nuestro proyecto de Django, solo si no se ha creado

    ```bash
    python manage.py createsuperuser
    ```

    Ingrese Username, Email address y Password.

7. Levantar el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    ```bash
    python manage.py runserver
    ```

    Es hora de ir al navegador y en una pestaña nueva navegar hacia "http://127.0.0.1:8000"

