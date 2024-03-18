all: test

hello:
	echo "HOHOHOH"
	echo "LOLOLOLO"

test:
	pytest -sv tests/test_lab3.py
clean:
	rm -rf ./pytest_cache