#!/usr/bin/env python3
from pathlib import Path
import sys

here = Path(__file__).resolve()

for p in here.parents:
    if (p / "mit_ocw_exercises").exists():
        sys.path.insert(0, str(p))
        break
