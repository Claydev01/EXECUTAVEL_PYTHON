import sys
from cx_Freeze import setup, Executable 

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "MyApp",
    version = "0.1",
    description = "MyApp",
    options = {"build_exe": build_exe_options},
    executables = [Executable("App.py", base=base)]
)