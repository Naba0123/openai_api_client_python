.PHONY: init up

.DEFAULT_GOAL := up

init:
	# copy env
	cp .env.example .env
	# install library
	pip install openai python-dotenv

up:
	python main.py
