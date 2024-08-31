# This is where you will configure how your app works.
# This is also a good place to get your .env variables, and throw an exception if a critical variable is not found.

import platform
import os

BASEDIR = os.getcwd()

APP_TITLE = 'Tkinter App'
OS_IS_WINDOWS = platform.system() == "Windows"
WINDOW_SIZE = "365x220" if platform.system() == "Windows" else "440x220" 
RESIZABLE_WINDOW_X = True
RESIZABLE_WINDOW_Y = True

# App icon
APP_ICON_NAME = 'app.png'
APP_ICON_PATH = os.path.join( BASEDIR, APP_ICON_NAME )

# Dynamic configuration file settings
CONFIG_FILE_NAME = 'config.json'
CONFIG_FILE_PATH = os.path.join( BASEDIR, CONFIG_FILE_NAME )
CONFIG_TEMPLATE = {
            "source_folder_path": "",
            "destination_folder_path": "",
            # REVIEW: not using it anymore, fetching file list from the functions instead
            # "mod_list": [
                # REF: Example mod list item
                # {
                #   "folder_name": "",
                #   "files": []
                # }
            # ],
        }
