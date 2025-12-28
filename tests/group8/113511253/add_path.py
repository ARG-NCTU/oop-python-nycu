import sys
import os

def add_path():
    """
    Add the project root directory to sys.path so that
    modules like 'lec9_inheritance' can be imported.
    """
    # 取得目前檔案 (add_path.py) 的絕對路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 往上找 3 層回到專案根目錄 (假設結構是 tests/group8/113511253)
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
