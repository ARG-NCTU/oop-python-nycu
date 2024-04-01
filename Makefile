all: test

hello:
	echo "Hello, world"
	echo "Hi"
test:
	pytest -sv tests/test_lab3.py

clean:
	rm -rf ./pytesy_cache

