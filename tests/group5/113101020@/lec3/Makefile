# Makefile for dua_cheer project

PYTHON := python3
PYTEST := pytest

.PHONY: all test run clean

# 預設目標：執行測試
all: test

# 執行 pytest
test:
	$(PYTEST)

# 直接執行主程式
run:
	$(PYTHON) dua_cheer.py

# 清除快取與編譯檔
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
