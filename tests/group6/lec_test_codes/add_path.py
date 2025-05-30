# tests/group9/add_path.py
import sys
import os

# 找到 src 資料夾，然後加入 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
