.PHONY: up init bash run down

up:
	docker compose up -d

init:
	# copy env
	cp .env.example .env

	docker compose exec python apt update
	docker compose exec python apt install -y make
	# install library
	docker compose exec python pip install openai python-dotenv

bash:
	docker compose exec -it python bash

run:
	docker compose exec python python main.py

down:
	docker compose down
