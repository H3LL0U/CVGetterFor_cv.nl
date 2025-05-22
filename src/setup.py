from cx_Freeze import setup, Executable

build_options = {'packages':[], 'excludes':[]}
import sys
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('src/main.py', base=base)
]

setup(name = 'CVgetter', version = '1.0.1' , description = 'Simple app to get your CV from the cv.nl',
      options = {'CVGetter.exe':build_options},
      executables = executables
      )