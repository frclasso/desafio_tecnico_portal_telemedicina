# Desafio Técnico Portal Telemedicina



Faça download do projeto
------------------------
- $ git clone https://github.com/frclasso/desafio_tecnico_portal_telemedicina.git



Rodando via docker
------------------
- $ docker-compose up -d --build
- $ docker-compose run app sh -c "python manage.py createsuperuser"
- $ docker-compose run app sh -c "python manage.py makemigrations"
- $ docker-compose run app sh -c "python manage.py migrate"


End points
----------
- http://localhost:8000/api/core/register/
- http://localhost:8000/api/core/login/
- http://localhost:8000/api/core/logout/

JSON Data Payloads
------------------
- Para inserir dados utilizar o arquivo localzado em app/core/api/utils.jon

Testando
--------
- $ docker-compose run app sh -c "python manage.py test && flake8"
