import sys
import os

current_dir = os.path.abspath(os.path.dirname(__file__))  
project_root = os.path.abspath(os.path.join(current_dir, '../../src'))  

for path in [project_root, current_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)