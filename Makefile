.PHONY: env-start env-end migrate fill analyse

env-start:
        docker-compose -f ./docker-compose.yaml up -d

env-end:
        docker-compose -f ./docker-compose.yaml down

migrate:
        python3 script.py migrate

fill:
        python3 script.py fill

analyse:
        python3 SQL_Statements.py
