#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Name: scrollable_frame_example.py
  @Author: fcarbajo
  @Site: https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/scrollable_frame_example.py
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


class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master, item_list, command=None, **kwargs):
    super().__init__(master, **kwargs)

    self.command = command
    self.checkbox_list = []
    for i, item in enumerate(item_list):
      self.add_item(item)

  def add_item(self, item):
    checkbox = customtkinter.CTkCheckBox(self, text=item)
    if self.command is not None:
      checkbox.configure(command=self.command)
    checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
    self.checkbox_list.append(checkbox)

  def remove_item(self, item):
    for checkbox in self.checkbox_list:
      if item == checkbox.cget("text"):
        checkbox.destroy()
        self.checkbox_list.remove(checkbox)
        return

  def get_checked_items(self):
    return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class ScrollableRadiobuttonFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master, item_list, command=None, **kwargs):
    super().__init__(master, **kwargs)

    self.command = command
    self.radiobutton_variable = customtkinter.StringVar()
    self.radiobutton_list = []
    for i, item in enumerate(item_list):
      self.add_item(item)

  def add_item(self, item):
    radiobutton = customtkinter.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
    if self.command is not None:
      radiobutton.configure(command=self.command)
    radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
    self.radiobutton_list.append(radiobutton)

  def remove_item(self, item):
    for radiobutton in self.radiobutton_list:
      if item == radiobutton.cget("text"):
        radiobutton.destroy()
        self.radiobutton_list.remove(radiobutton)
        return

  def get_checked_item(self):
    return self.radiobutton_variable.get()


class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master, command=None, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(0, weight=1)

    self.command = command
    self.radiobutton_variable = customtkinter.StringVar()
    self.label_list = []
    self.button_list = []

  def add_item(self, item, image=None):
    label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
    button = customtkinter.CTkButton(self, text="Command", width=100, height=24)
    if self.command is not None:
      button.configure(command=lambda: self.command(item))
    label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
    button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
    self.label_list.append(label)
    self.button_list.append(button)

  def remove_item(self, item):
    for label, button in zip(self.label_list, self.button_list):
      if item == label.cget("text"):
        label.destroy()
        button.destroy()
        self.label_list.remove(label)
        self.button_list.remove(button)
        return


class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    self.title("CTkScrollableFrame example")
    self.grid_rowconfigure(0, weight=1)
    self.columnconfigure(2, weight=1)

    # create scrollable checkbox frame
    self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,
                                 item_list=[f"item {i}" for i in range(50)])
    self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
    self.scrollable_checkbox_frame.add_item("new item")

    # create scrollable radiobutton frame
    self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500, command=self.radiobutton_frame_event,
                                     item_list=[f"item {i}" for i in range(100)],
                                     label_text="ScrollableRadiobuttonFrame")
    self.scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
    self.scrollable_radiobutton_frame.configure(width=200)
    self.scrollable_radiobutton_frame.remove_item("item 3")

    # create scrollable label and button frame
    current_dir = os.path.dirname(os.path.abspath(__file__))
    self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
    self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
    for i in range(20):  # add items with images
      self.scrollable_label_button_frame.add_item(f"image and item {i}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "images", "chat_light.png"))))

  def checkbox_frame_event(self):
    print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

  def radiobutton_frame_event(self):
    print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

  def label_button_frame_event(self, item):
    print(f"label button frame clicked: {item}")


if __name__ == "__main__":
  customtkinter.set_appearance_mode("dark")
  app = App()
  app.mainloop()
