DOCKER_COMPOSE_FILES = -f docker-compose.yml
ifeq ($(WITH_MOCKS), true)
	DOCKER_COMPOSE_FILES += -f docker-compose.mocks.yml
endif

ifeq ($(WITH_LOCUSTIO), true)
	DOCKER_COMPOSE_FILES += -f docker-compose.locustio.yml
endif

DOCKER_COMPOSE_FILES += -f docker-compose.python.yml
DOCKER_COMPOSE=docker-compose $(DOCKER_COMPOSE_FILES)

build: ## Build the docker containers
	docker build -t ubuntu:xenial -f docker/mongo/Dockerfile .
	docker build -t grubykarol/locust:0.10.0-python3.6-alpine3.9 -f docker/locustio/Dockerfile .
	docker build -t cim/mocks-mountebank -f docker/mountebank/Dockerfile .
	docker build -t cim/python -f docker/python/Dockerfile .
start:
	$(DOCKER_COMPOSE) up -d

stop:
	$(DOCKER_COMPOSE) stop

start-with-mocks: ## start service with mocking enabled
	WITH_MOCKS=true make start

start-with-locustio: ## start service with mocking enabled
	WITH_MOCKS=true make start
	WITH_LOCUSTIO=true make start

stop-with-mocks: ## start service with mocking enabled
	WITH_MOCKS=true make stop

stop-with-locustio: ## start service with mocking enabled
	WITH_MOCKS=true make stop
	WITH_LOCUSTIO=true make stop

start-without-mocks: ## start service without mocking
	WITH_MOCKS=false make start

.SILENT: help
help: ## Show this help message
	set -x
	echo "Usage: make [target] ..."
	echo ""
	echo "Available targets:"
	grep ':.* ##\ ' ${MAKEFILE_LIST} | awk '{gsub(":[^#]*##","\t"); print}' | column -t -c 2 -s $$'\t' | sort
