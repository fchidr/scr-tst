#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  @Name: frontend.py
  @Author: fcarbajo
  @Site: 
  @Descripción: Pruebas de TtkBootstrap
  @Usage:
"""

__author__ = 'Fernando J. Carbajo'
__version__ = '1.0.0'
__date__ = '2023-10-07'

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

import backend as be
import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.rowconfigure(3, weight=1)

        self.new_note_btn = ctk.CTkButton(
            self,
            text="New Note",
            width=250,
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().new_note
        )
        self.new_note_btn.grid(
            column=0,
            row=0,
            padx=10,
            pady=5
        )

        self.save_note_btn = ctk.CTkButton(
            self,
            text="Save Note",
            width=250,
            fg_color="#307C39",
            hover_color="#245E2B",
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().save_note
        )
        self.save_note_btn.grid(
            column=0,
            row=1,
            padx=10,
            pady=5
        )

        self.delete_note_btn = ctk.CTkButton(
            self,
            text="Delete Note",
            width=250,
            fg_color='#C73E1D',
            hover_color='#8C2D15',
            font=self.winfo_toplevel().button_font,
            command=self.winfo_toplevel().delete_note,
            state='disabled'
        )
        self.delete_note_btn.grid(
            column=0,
            row=2,
            padx=10,
            pady=5
        )

        self.notes_list = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.notes_list.grid(
            column=0,
            row=3,
            sticky="nsew"
        )


class MainWindow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.title = ctk.CTkEntry(
            self,
            fg_color="transparent",
            border_width=0,
            font=self.winfo_toplevel().title_font
        )
        self.title.grid(
            column=0,
            row=0,
            padx=(0, 5),
            pady=5,
            sticky="ew"
        )

        self.body = ctk.CTkTextbox(
            self,
            fg_color="transparent",
            font=self.winfo_toplevel().body_font,
            wrap="word",
            activate_scrollbars=False
        )
        self.body.grid(
            column=0,
            row=1,
            sticky="nsew",
            columnspan=2
        )


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Create local db and table if they don't exist
        be.create_notes_table()

        # Appearance
        ctk.set_appearance_mode('dark')
        self.title('Notes')
        self.geometry('1000x600')
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Fonts
        self.title_font = ctk.CTkFont(
            family="Arial",
            size=40,
            weight='bold'
        )
        self.body_font = ctk.CTkFont(
            family="Helvetica",
            size=16
        )
        self.button_font = ctk.CTkFont(
            family="Helvetica",
            size=13
        )

        # Sidebar
        self.sidebar = Sidebar(self, fg_color="transparent")
        self.sidebar.grid(
            column=0,
            row=0,
            padx=(10, 5),
            pady=10,
            sticky="ns"
        )

        # Main Window
        self.main_window = MainWindow(self, fg_color="transparent")
        self.main_window.grid(
            column=1,
            row=0,
            padx=(5, 10),
            pady=10,
            sticky="nsew"
        )

        # Start a New Note
        self.new_note()

# Load buttons for any existing notes into the sidebar
        self.load_notes()

    def new_note(self):
        self.current_note_id = None
        self.main_window.title.delete(0, ctk.END)
        self.main_window.body.delete('1.0', ctk.END)
        self.main_window.title.insert(0, "New Note")
        self.main_window.body.focus_set()
        self.sidebar.delete_note_btn.configure(state='disabled')

    def save_note(self):
        title = self.main_window.title.get()
        body = self.main_window.body.get('1.0', ctk.END)

        if self.current_note_id is None:
            be.create_note(title, body)
        else:
            be.update_note(self.current_note_id, title, body)

        note_id = be.get_last_note_id()
        self.current_note_id = note_id

        self.load_notes()
        self.sidebar.delete_note_btn.configure(state='normal')

    def delete_note(self):
        if self.current_note_id is not None:
            be.delete_note(self.current_note_id)
            self.load_notes()
            self.new_note()

    def load_note_content(self, note_id):
        note = be.get_note(note_id)
        if note:
            note_title = note[1]
            note_body = note[2]
            self.current_note_id = note_id
            self.main_window.title.delete(0, ctk.END)
            self.main_window.body.delete('1.0', ctk.END)
            self.main_window.title.insert(0, note_title)
            self.main_window.body.insert('1.0', note_body)
            self.sidebar.delete_note_btn.configure(state='normal')

    def load_notes(self):
        for child in self.sidebar.notes_list.winfo_children():
            child.destroy()

        notes = be.get_all_notes()

        for i, note in enumerate(notes):
            note_id = note[0]
            note_title = note[1]
            button = ctk.CTkButton(
                self.sidebar.notes_list,
                text=note_title,
                width=250,
                fg_color="transparent",
                font=self.button_font,
                command=lambda id=note_id: self.load_note_content(id)
            )
            button.grid(column=0, row=i, padx=10, pady=5)