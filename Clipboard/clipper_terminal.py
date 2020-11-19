#! python3

'''
@author: Max Felius
@email: max@felius.nl

Small python script for storing terminal output directly onto the clipboard

bash alias

alias c="python3 ~/toolbox/clipper.py"

'''

# imports
import sys
import pyperclip

#input form stdin
info = input()

#copy to clipboard
pyperclip.copy(info)
