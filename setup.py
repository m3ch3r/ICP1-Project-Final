# Note that this code is not mine.
# Credit: https://cx-freeze.readthedocs.io/en/latest/setup_script.html

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {'packages' : ["os"], 'include_files' : ["calcTest.py", "createWidgets.py", "gridDraw.py", "README.md", "logo.ico"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Python Graphing Calculator",
    version = "1.0",
    description = """Authored by: Braden Franklin""",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, shortcutName="Graphing Calculator",
        shortcutDir="DesktopFolder")]
)