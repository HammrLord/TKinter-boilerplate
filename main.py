from tkinter import Tk, ttk, filedialog, Frame, StringVar, IntVar, Variable, END, PhotoImage, Listbox

from actions import *
import settings

import os
import json
import platform
import logging

logging.basicConfig(filename='app.log', filemode='a', level=logging.DEBUG, format="[%(asctime)s](%(name)s - %(levelname)s): %(message)s")
logging.info('This will get logged to a file', exc_info=True)

class TKinterApp:
    def __init__(self):

        # Constants
        self.app_title = settings.APP_TITLE
        self.app_window_size = settings.WINDOW_SIZE
        self.config_file_name = settings.CONFIG_FILE_NAME
        self.app_icon = settings.APP_ICON_PATH
        self.app_base_dir = settings.BASEDIR
        self.os_is_windows = settings.OS_IS_WINDOWS

        self.selected_mod_files = []

        # load config
        self.read_config()

        # initiate Tkinter
        self.root = Tk()
        self.root.title(self.app_title)
        self.root.geometry(self.app_window_size)
        self.root.resizable(False, False)
        # cannot be used with pyinstaller
        # self.app_icon = PhotoImage(file=os.path.abspath(self.app_icon))
        self.app_icon = PhotoImage(file=self.app_icon)
        self.root.iconphoto(True, self.app_icon)
        # self.root.iconbitmap(os.path.abspath(self.app_icon))

        # Load styles
        self.get_styles()

        # BOOKMARK: NOTEBOOK
        # Create the notebook (tabs container)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(column=0, columnspan=6, row=0, rowspan=6)
        # Create frames for each tab
        self.manage_frame = ttk.Frame(self.notebook)
        self.settings_frame = ttk.Frame(self.notebook)
        # Add tabs to the notebook
        self.notebook.add(self.manage_frame, text="Manage")
        self.notebook.add(self.settings_frame, text="Settings")


        # MSG: Manage tab layout

        self.manage_content_frame = ttk.Frame(self.manage_frame)
        self.manage_content_frame.grid(column=0, columnspan=6, row=0, rowspan=6)

        # TAB LAYOUT


        # Run the main loop
        self.root.mainloop()
    
    # WARN:
    def read_config(self):
        try:
          with open(self.config_file_name, 'r', encoding='utf-8') as f:
            self.app_config = json.load(f)
        except FileNotFoundError:
          # If file not found, create it with default data
          with open(self.config_file_name, 'w', encoding='utf-8') as f:
            json.dump(self.get_config_template(), f, indent=4)
          self.app_config = self.get_config_template()

        return self.app_config

    # WARN:
    def write_config(self, key, data):
        keys = key.split('.')
        config = self.read_config()
        d = config
        for k in keys[:-1]:
            d = d[k]
        d[keys[-1]] = data
        with open(os.path.abspath(self.config_file_name), "w") as file:
            json.dump(config, file, indent=4)
    
    # WARN:
    def get_config_template(self):
        return settings.CONFIG_TEMPLATE

     # WARN:
    def get_styles(self):
        # TODO: replace this with a function call
        button_style = ttk.Style()
        button_style.configure(
            "Custom1.TButton",
            font=("Calibri", 8, "normal"),
            foreground="black" if self.os_is_windows else "white",
            background="#278ef0",
            width="11",
        )
        button_style.map(
            "Custom1.TButton",
            foreground=[("active", "!disabled", "black")],
            background=[("active", "!disabled", "#a9d3fa")],
        )
        return


if __name__ == "__main__":
    mm = ModManager()
