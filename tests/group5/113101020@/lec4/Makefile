.PHONY: all test run

# 設定 Python 與檔案路徑
PY := python3
CORE := dua_lec4.py
TEST_PATTERN := test_dua_lec4.py

all: test

# 執行 pytest（預設偵測當前目錄下測試檔）
test:
	$(PY) -m pytest $(TEST_PATTERN)

# 用 Python 執行主程式	run:
	$(PY) $(CORE)

