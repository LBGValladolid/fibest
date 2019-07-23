# FiBEST

FiBEST es una aplicación Django para facilitar y gestionar las tareas de FiBEST así como ser la cara
pública del foro en la red para usuarios y empresas.

## Instalar

FiBEST usa Docker Compose para gestionar su entorno.

```
docker-compose up --build
```

Debería arrancar la web en modo producción desde cero

Si quieres desarrollar es más fácil usar Pipenv

```
pipenv install
pipenv shell
python manage.py runserver
```

La base de datos y los CV están en volúmenes de Docker

## Crear bases de datos

```
docker-compose run django python manage.py makemigrations fibest
docker-compose run django python manage.py migrate
```

# Crear superusuario

Los superusuarios tienen acceso a Django Admin

```
docker-compose run django python manage.py createsuperuser
```

Django Admin: /admin