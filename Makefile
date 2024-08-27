#!/usr/bin/make

# run docker services
.PHONY: deploy
deploy: build
	docker compose up -d

# stop all docker services
.PHONY: stop
stop:
	docker compose down

# build python reporter package
.PHONY: build-reporter
build-reporter:
	cp ${CURDIR}/pyproject.reporter.toml ${CURDIR}/pyproject.toml 
	poetry build --no-cache
	rm -f ${CURDIR}/pyproject.toml

# build python dashboard package
.PHONY: build-dashboard
build-dashboard:
	cp ${CURDIR}/pyproject.dashboard.toml ${CURDIR}/pyproject.toml
	poetry build --no-cache
	rm -f ${CURDIR}/pyproject.toml

# build all python packages and custom docker images
.PHONY: build
build: build-reporter build-dashboard
	docker compose build

# reset the docker environment
.PHONY: docker-reset
docker-reset:
	docker rm -f $$(docker ps -a -q); \
	docker rmi -f $$(docker images -q); \
	docker volume rm $$(docker volume ls -q); \
	docker system prune -f