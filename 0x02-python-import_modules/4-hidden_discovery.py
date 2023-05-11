#!/usr/bin/python3
import sys
sys.path.append('/path/to/module/https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc')
import hidden_4

for name in sorted(dir(hidden_4)):
    if not name.startswith("__"):
        print(name)
