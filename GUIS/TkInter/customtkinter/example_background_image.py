#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Name: complex_example.py
  @Author: fcarbajo
  @Site: https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/complex_example.py
  @Descripción: Pruebas de CustomTkinter
  @Usage:
"""

__author__ = 'Fernando J. Carbajo'
__version__ = '1.0.0'
__date__ = '2025-10-17'

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

# libraries Import
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
  width = 900
  height = 600

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.title("CustomTkinter example_background_image.py")
    self.geometry(f"{self.width}x{self.height}")
    self.resizable(False, False)

    # load and create background image
    current_path = os.path.dirname(os.path.realpath(__file__))
    self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/images/bg_gradient.jpg"),
                         size=(self.width, self.height))
    self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
    self.bg_image_label.grid(row=0, column=0)

    # create login frame
    self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
    self.login_frame.grid(row=0, column=0, sticky="ns")
    self.login_label = customtkinter.CTkLabel(self.login_frame, text="CustomTkinter\nLogin Page",
                          font=customtkinter.CTkFont(size=20, weight="bold"))
    self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
    self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
    self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
    self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
    self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
    self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
    self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    # create main frame
    self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                         font=customtkinter.CTkFont(size=20, weight="bold"))
    self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
    self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
    self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

  def login_event(self):
    print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

    self.login_frame.grid_forget()  # remove login frame
    self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

  def back_event(self):
    self.main_frame.grid_forget()  # remove main frame
    self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
  app = App()
  app.mainloop()
