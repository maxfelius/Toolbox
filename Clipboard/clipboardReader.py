#! python3
'''
@author: Max Felius
@email: max@felius.nl

This script is used to take the terminal input and put it onto the clipboard

-Go to your home directory (~/) and open .bash_profile
-Add a new line: alias c='python3 clipboardReader.py'

'''

#imports
import pyperclip
try:
    pyperclip.copy(input())
except EOFError:
    print('Can not copy input to clipboard')
