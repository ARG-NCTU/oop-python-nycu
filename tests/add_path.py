# tests/add_path.py

import sys
import os


def add_path():
    """
    把專案根目錄和 tests/group1 加進 sys.path，
    讓測試可以 import 到 lecX_*.py 檔案。
    """
    # 目前這個檔案所在資料夾：.../oop-python-nycu/tests
    tests_dir = os.path.dirname(os.path.abspath(__file__))

    # 專案根目錄：.../oop-python-nycu
    project_root = os.path.dirname(tests_dir)

    # group1 資料夾：.../oop-python-nycu/tests/group1
    group1_dir = os.path.join(tests_dir, "group1")

    # 依序塞進 sys.path（前面優先）
    for path in (project_root, tests_dir, group1_dir):
        if path not in sys.path:
            sys.path.insert(0, path)
