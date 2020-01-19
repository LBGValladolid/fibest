# FiBEST

FiBEST es una aplicación Django para facilitar y gestionar las tareas de FiBEST así como ser la cara
pública del foro en la red para usuarios y empresas.

## Instalar

FiBEST usa Docker Compose para gestionar su entorno.

Se usan variables de entorno, están subidas en el servidor en la propia carpeta de fibest
```
source .env; docker-compose up --build
```

Debería arrancar la web en modo producción desde cero

Si quieres desarrollar es más fácil usar Pipenv

```
pipenv install
pipenv shell
python manage.py runserver
```

La base de datos y los CV están en volúmenes de Docker

## Ficheros estáticos

```
docker-compose run django python manage.py collectstatic
```

## Crear bases de datos / Modificar

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

# Backup y restore de la BD

backup

```
docker run --rm -v fibest_data:/volume -v ~/backup:/backup alpine tar -cjf /backup/fibest-data.tar.bz2 -C /volume ./
```

restore

```
docker run --rm -v fibest_data:/volume -v /home/backup:/backup alpine sh -c "rm -rf /volume/* /volume/--?* /volume/.[!.]* ; tar -C /volume/ -xjf /backup/fibest-data.tar.bz2"
```