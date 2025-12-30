#!/usr/bin/env python3
"""
Pytest configuration for 113511086's tests.
Adds the src directory to Python path so tests can import from mit_ocw_exercises.
"""

import os
import sys
import pytest

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


def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )


@pytest.fixture(autouse=True)
def reset_rabbit_tag():
    """Reset Rabbit class tag counter before each test to ensure consistent RIDs."""
    # Try to reset the tag in all possible module locations
    import sys

    # Reset in local module if it exists
    if 'lec9_inheritance' in sys.modules:
        try:
            sys.modules['lec9_inheritance'].Rabbit.tag = 27
        except (AttributeError, KeyError):
            pass

    # Reset in mit_ocw_exercises.lec9_inheritance if it exists
    if 'mit_ocw_exercises.lec9_inheritance' in sys.modules:
        try:
            sys.modules['mit_ocw_exercises.lec9_inheritance'].Rabbit.tag = 27
        except (AttributeError, KeyError):
            pass

    yield

    # Reset again after the test (in case test execution changes it)
    if 'lec9_inheritance' in sys.modules:
        try:
            sys.modules['lec9_inheritance'].Rabbit.tag = 27
        except (AttributeError, KeyError):
            pass

    if 'mit_ocw_exercises.lec9_inheritance' in sys.modules:
        try:
            sys.modules['mit_ocw_exercises.lec9_inheritance'].Rabbit.tag = 27
        except (AttributeError, KeyError):
            pass
