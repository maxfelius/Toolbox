#! python3
'''
@author: Max Felius
@email: maxfelius@hotmail.com

Latex Table Creator

'''

#imports
import numpy as np
import sys

class LatexTable(object):
	"""docstring for LatexTable"""
	def __init__(self, arg):
		'''INIT'''
		self.arg = arg

		# standard options
		self.table_position = None
		self.output = None

		# initialize standard options
		self.standard_options()

	def standard_options(self):
		self.table_position = '[h1]'
		self.output = 'Latex'
			

	def __str__(self):
		'''print string'''
		print('This is a class for Latex Tables')

	def options(self,options):
		'''options input should be a dictionary'''
		if not isinstance(options,dict):
			print('Please use a dictionary as input to change the options')
		else:
			pass


def _test():
	pass

if __name__ == '__main__':
	_test()
		