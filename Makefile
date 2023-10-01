default: 
	@echo "Comandos disponíveis"
	@echo "make build           - Cria containers caso não os tenha"
	@echo "make makemigrations  - Cria migrations"
	@echo "make migrate         - Executa migrations"
	@echo "make createsuperuser - Criar um usuario"
	@echo "make start           - Inicializa container, e executa serviço Django"
	@echo "make stop            - Encerra execução dos containers BD e Django"

build:
ifeq ("$(wildcard .env.dev)","") 
	cp .env.dev-example .env.dev
	@echo "New file .env.dev created" 		
endif
	docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build

bash:
	docker exec -ti therapy_scheduler bash

makemigrations:
	docker exec -ti therapy_scheduler python manage.py makemigrations --no-input
	docker exec -ti therapy_scheduler python manage.py migrate

createsuperuser:
	docker exec -ti therapy_scheduler python manage.py create_super_admin

start:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti therapy_scheduler python manage.py runserver 0.0.0.0:8000

stop:
	docker-compose -f docker-compose-dev.yaml stop 

clearmigrations:
	docker-compose -f docker-compose-dev.yaml find . -path "/migrations/.py" -not -name "_init_.py" -delete