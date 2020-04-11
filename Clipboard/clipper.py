#! python3

'''
@author: Max Felius
@email: maxfelius

Clipboard storer
- Script that stores clipboard items
- Should save output of terminal command to clipboard
- easy pasting into terminal

Usage information:
clipper.py list
clipper.py save <keyword>
clipper.py <keyword>
'''

#imports
import shelve
import pyperclip
import sys

#open/create the database
ClippperShelf = shelve.open('database')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	ClippperShelf[sys.argv[2]] = pyperclip.paste()

#list the keywords and load content
elif len(sys.argv) == 2:
	#list the keywords
	if sys.argv[1].lower() == 'list':
		print(str(list(ClippperShelf.keys())))
	elif sys.argv[1] in ClippperShelf:
		pyperclip.copy(ClippperShelf[sys.argv[1]])

ClippperShelf.close()