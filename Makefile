SHELL := /bin/bash

build:
	cd deploy/ && docker-compose build
up:
	cd deploy/ && docker-compose up
down:
	cd deploy/ && docker-compose down --remove-orphans
