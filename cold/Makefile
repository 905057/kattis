all: style-check type-check unittest test
	@echo "All done..."

unittest:
	pytest -v test_cold.py
	
test:
	@cat 1.in | python cold.py | diff - 1.ans
	@cat 2.in | python cold.py | diff - 2.ans
	@echo "All local test passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

kattis:
	@kattis -f cold.py