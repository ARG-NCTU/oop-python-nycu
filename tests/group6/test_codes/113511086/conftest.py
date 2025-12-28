#!/usr/bin/env python3
"""
Pytest configuration for 113511086's tests.
Adds the src directory to Python path so tests can import from mit_ocw_exercises.
"""

import os
import sys

# Get the directory containing this conftest.py file (student's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add student's directory FIRST so their implementations are used
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Navigate up to project root: 113511086 -> test_codes -> group6 -> tests -> project_root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

# Get the src directory (fallback)
src_dir = os.path.join(project_root, 'src')

# Add src directory as fallback
if src_dir not in sys.path:
    sys.path.append(src_dir)

if project_root not in sys.path:
    sys.path.append(project_root)
