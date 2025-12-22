#!/usr/bin/env python3
"""
Pytest configuration for 113511086's tests.
Adds the src directory to Python path so tests can import from mit_ocw_exercises.
"""

import os
import sys

# Get the directory containing this conftest.py file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to project root: 113511086 -> test_codes -> group6 -> tests -> project_root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

# Get the src directory
src_dir = os.path.join(project_root, 'src')

# Add to Python path if not already present
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

if project_root not in sys.path:
    sys.path.insert(0, project_root)
