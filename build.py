from cx_Freeze import setup, Executable

executables = [
    Executable('main.py', base='Win32GUI')
]

setup(name='UNIQUE_TAV_HEAD_PATCHER',
      version='1.0',
      executables=executables)