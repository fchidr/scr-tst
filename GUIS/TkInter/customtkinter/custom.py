#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Name: custom.py
  @Author: fcarbajo
  @Site: 
  @Descripción: Pruebas de TtkBootstrap
  @Usage:
"""

__author__ = 'Fernando J. Carbajo'
__version__ = '1.0.0'
__date__ = '2025-05-15'

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

# https://customtkbuilder.com/

# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Main")
window.geometry("800x350")
window.configure(bg="#FFFFFF")


radio_var = IntVar()

RadioButton_id6 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=6,
    text="Radio Button 2",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    )
RadioButton_id6.place(x=80, y=220)
Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Test",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id1.place(x=350, y=310)
Entry_id3 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id3.place(x=170, y=80)
Label_id2 = customtkinter.CTkLabel(
    master=window,
    text="Título",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id2.place(x=70, y=80)
Checkbox_id4 = customtkinter.CTkCheckBox(
    master=window,
    text="Test",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    )
Checkbox_id4.place(x=80, y=150)
RadioButton_id5 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=5,
    text="Radio Button 1",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    )
RadioButton_id5.place(x=80, y=190)



#run the main loop
window.mainloop()
