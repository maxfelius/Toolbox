#! python3
'''
@author: Max Felius
@email: maxfelius@hotmail.com

See 'input.py' for more information
'''

#imports
import PyPDF2
import input_copy as input

class splitpdf:
	def __init__(self,dict_file):
		#import a string with the bundled pdf
		self.input_content = dict_file['input_file']
		
                #import list with all the specification for the output format
		self.output_content = dict_file['output_files']
                
                #Load the pdf that has to be splitted and create a pdf object from it
		pdfFileobj = open(self.input_content, 'rb')
		self.pdfreader = PyPDF2.PdfFileReader(pdfFileobj)

	def write_pdf(self):
		#Goes through the list filled with dicts
		for file in self.output_content:
			#create the new file
			pdfOutputfile = open(file['name']+'.pdf','wb')

			#create the pdf object for manipulating the pages
			pdfWriter = PyPDF2.PdfFileWriter()

			#add pages to the pdfWriter object
			for page_num, rot in zip(file['pages'],file['rotation']):

				#python starts at 0 while pdf viewers start at 1
				pageObj = self.pdfreader.getPage(page_num-1)

				#rotate the pages
				pageObj.rotateClockwise(rot*90)

				#add page to object
				pdfWriter.addPage(pageObj)

			#finish writing the pdf to file
			print('Created new pdf {}.pdf'.format(file['name']))
			pdfWriter.write(pdfOutputfile)
			pdfOutputfile.close()

if __name__ == '__main__':
    splitpdf(input.content).write_pdf()
