all:test

hello:
	echo "Hello World"
	echo "This line will print if the file hello does not exist"

test:
	pytest -sv tests/team_ta/newTest/new_test_food.py

clean:
	rm -rf ./pytest_cache
