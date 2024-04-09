import subprocess


files = ["main.py"]
console = "--disable-console"
mode = "--onefile"
plugin = "--enable-plugin=pyqt5" 


subprocess.run(["python", "-m", "nuitka", console, mode, plugin] + files)

# Console command
# python -m nuitka --disable-console --onefile --enable-plugin=pyqt5 main.py

# Create .py file from .ui file
# python -m PyQt5.uic.pyuic -x test.ui -o test.py