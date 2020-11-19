#! python3
'''
@author: Max Felius
@email: maxfelius@hotmail.com

How to use this Tool

1. After 'input_file' set the name of the pdf that has to be splitted

2. copy the piece of code into the list (i.e. between the [ ]). 
Each piece of code will be a new pdf file
Rotation set to 0 means that the page will not get rotated

{   'name':'pdf name',
    'pages':[],
    'rotation':[]},

3. Run 'pdf_splitter.py'
'''

content = {'input_file':'Wijnproeverij.pdf',
           'output_files':[
           {'name':'Wijnproeverij_documenten',
            'pages':[1,3,1,3,1,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            'rotation':[0]*20}
            ]}

            
             
            

