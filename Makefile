default: 
	@echo "Comandos disponíveis"
	@echo "make build           			- Cria containers caso não os tenha"
	@echo "make connect           			- Connect to AWS"
	@echo "make makemigrations  			- Cria migrations"
	@echo "make migrate         			- Executa migrations"
	@echo "make create_super_admin			- Criar um usuario super admin"
	@echo "make create_basic_values 		- Popula o banco de dados com dados básicos"
	@echo "make create_custom_permissions  	- Popula o banco com permissões"
	@echo "make create_fake_data 			- Popula o banco com boilerplate"
	@echo "make start           			- Inicializa container, e executa serviço Django"
	@echo "make stop            			- Encerra execução dos containers BD e Django"
	@echo "make clearmigrations 			- Limpa todas as migrations"@echo "make export_requirements 		- Exporta as dependencias do Poetry para um arquivo requirements.txt"

build:
ifeq ("$(wildcard .env.dev)","") 
	cp .env.dev-example .env.dev
	@echo "New file .env.dev created" 		
endif
	docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build

bash:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti therapy_scheduler bash

makemigrations:
	docker exec -ti therapy_scheduler python manage.py makemigrations --no-input
	docker exec -ti therapy_scheduler python manage.py migrate

create_super_admin:
	docker exec -ti therapy_scheduler python manage.py create_super_admin

create_basic_values:
	docker exec -ti therapy_scheduler python manage.py create_basic_values

create_custom_permissions:
	docker exec -ti therapy_scheduler python manage.py create_custom_permissions

create_fake_data:
	docker exec -ti therapy_scheduler python manage.py create_fake_data

start:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti therapy_scheduler python manage.py runserver_plus 0.0.0.0:8000

stop:
	docker-compose -f docker-compose-dev.yaml stop 

test:
	docker exec -ti therapy_scheduler python manage.py test 

clearmigrations:
	docker exec -ti therapy_scheduler find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

connect:
	ssh -i "teste-schedule.pem" ubuntu@ec2-3-23-182-8.us-east-2.compute.amazonaws.com

export_requirements:
	poetry export --output requirements.txt --without-hashes --with dev