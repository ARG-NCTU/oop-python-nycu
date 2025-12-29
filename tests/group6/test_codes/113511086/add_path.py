#!/usr/bin/env python3

import os
import sys
# Add current directory FIRST so student implementations are used
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Then add src directory as fallback
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 '../../../src'))
