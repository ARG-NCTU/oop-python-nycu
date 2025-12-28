import sys
import os

def add_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, current_dir)
    sys.path.insert(0, parent_dir)
