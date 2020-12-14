# Desafio Técnico Portal Telemedicina



Faça download do projeto
------------------------
$ git clone https://github.com/frclasso/desafio_tecnico_portal_telemedicina.git



Rodando via docker
------------------
$ docker-compose up -d --build
$ docker-compose run app sh -c "python manage.py createsuperuser"
$ docker-compose run app sh -c "python manage.py makemigrations"
$ docker-compose run app sh -c "python manage.py migrate"

Testando
--------
$  docker-compose run app sh -c "python manage.py test && flake8"
