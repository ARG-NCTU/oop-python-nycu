.PHONY: test clean

test:
	pytest -v

clean:
	rm -rf __pycache__ .pytest_cache

