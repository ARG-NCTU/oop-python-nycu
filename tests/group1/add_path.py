# add_path.py
import sys
import os

def add_path():
    """
    Automatically add the parent directory of this file
    to sys.path so that pytest can import student modules
    from GitHub Actions.
    """
    file_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(file_dir)

    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
