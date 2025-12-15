#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Name: custom.py
  @Author: fcarbajo
  @Site: 
  @Descripción: Pruebas de TtkBootstrap
  @Usage:
  Requiere https://pypi.org/project/customtkinter/ (https://github.com/TomSchimansky/CustomTkinter/)
"""

__author__ = 'Fernando J. Carbajo'
__version__ = '1.0.0'
__date__ = '2024-02-01'

import sys
import os
from pathlib import Path

script_path = Path(__file__).parent
script_base = Path(script_path).parent
script_libs = os.path.join(script_path, 'libs')
common_libs = f"{script_base}\\commons"

#print(f'{str(script_base) =}')
#print(f'{str(script_path) =}')
#print(f'{script_libs =}')
#print(f'{common_libs =}')

py_short_name = os.environ['PY_SHORT_NAME']
PYTHON_PROFILE = os.environ['PYTHON_PROFILE']
PY_NAME = (os.environ['PY_NAME'])
PYTHON_NAME_PROFILE = '{}\\{}'.format(PYTHON_PROFILE, PY_NAME)

py_full_version = "{}.{}.{}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
py_version = sys.version_info.major
pyv = '{}{}'.format(sys.version_info.major, sys.version_info.minor)

sys.path.insert(0, script_path)
sys.path.insert(1, script_libs)
sys.path.insert(2, common_libs)

from frontend import App

if __name__ == "__main__":
  app = App()
  app.mainloop()
