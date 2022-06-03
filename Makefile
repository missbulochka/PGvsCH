.PHONY: env-start env-end


env-start:
	docker-compose -f ./docker-compose.yaml up -d

env-end:
	docker-compose -f ./docker-compose.yaml down
