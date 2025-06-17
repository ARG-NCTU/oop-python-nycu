# Makefile for running pytest on test_dua_example.py

# 執行測試
test:
	pytest test_dua_example.py

# 移除 pytest 的暫存資料
clean:
	rm -rf __pycache__ .pytest_cache

# 預設目標（當只打 make 時會執行）
all: test
