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
---

End points
----------
- http://localhost:8000/api/core/register/
- http://localhost:8000/api/core/login/
- http://localhost:8000/api/core/logout/
----
  
- http://localhost:8000/api/core/speakers/ >> Listagem dos Palestrantes
- http://localhost:8000/api/core/speakers/<id> >> Detalhes do Palestrante
- http://localhost:8000/api/core/speakers/<id>/update/ >> Atualizar dados do Palestrante
- http://localhost:8000/api/core/speakers/<id>/delete/ >> Deletar Palestrante juntamente com as palestras
-----
- http://localhost:8000/api/core/lectures/ >> Listagem das Palestras
- http://localhost:8000/api/core/lectures/<id> >> Detalhes da Palestra
- http://localhost:8000/api/core/lectures/<id>/update/ >> Atualizar dados da Palestra
- http://localhost:8000/api/core/lectures/<id>/delete/ >> Deleta Palestra
-----

Filtrando por data
-------
http://localhost:8000/api/core/lectures/?data="2020-12-17"


JSON Data Payloads
------------------
- Para inserir dados utilizar o arquivo localzado em app/core/api/utils.jon
---

Testando
--------
- $ docker-compose run app sh -c "python manage.py test && flake8"
