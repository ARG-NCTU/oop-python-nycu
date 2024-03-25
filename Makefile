all:test
hello:
	echo "Hello World"
	echo "This line will print if the file hello does not exist" 
test:
	pytest -sv tests/test_lab3.py

clean:
	rm -rf ./pytest_cache

