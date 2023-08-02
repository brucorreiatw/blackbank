.PHONY : bddtests unittests tests testreport requestdebit requestcredit build run restart clean
ENV_TEST := True
export ENV_TEST

venv:
	python -m venv .venv
	. .venv/bin/activate 
	pip install -r blackapi/requirements.txt

unittests:
	python -m unittest discover blackapi/tests/unittests/ -v
	
bddtests:
	behave blackapi/tests/behavior/features

testreport:
	coverage run -m unittest discover blackapi/tests/unittests/
	coverage report 
	
requestdebit:
	curl -X POST -F "file=@blackapi/csv_sample/csv_example.csv" localhost:5000/invoice/create
	
requestcredit:
	curl --header 'Content-Type: application/json' --request POST --data '{ "debtId": "8291", "paidAt": "2022-06-09 10:00:00", "paidAmount": "100000.00", "paidBy": "John Doe" }' http://localhost:5000/payment/create

build:
	docker-compose build

run:
	docker-compose up -d 

stop:
	docker-compose down

logs:
	docker-compose logs -f

restart: stop run

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	rm ./temp/*

tests: venv unittests bddtests
