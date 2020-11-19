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

content = {'input_file':'mfelius_2019-10-16_17-19-45-247.pdf',
           'output_files':[
           {'name':'Assignment',
            'pages':[1,3,4],
            'rotation':[1,1,0]},

            {'name':'geologicalMap',
            'pages':[2,5,7],
            'rotation':[0,2,2]},

            {'name':'OutcropA',
            'pages':[9,11],
            'rotation':[1,1]},

            {'name':'OutcropB',
            'pages':[13,15,17,19,21],
            'rotation':[1,1,1,1,1]},

            {'name':'OutcropC',
            'pages':[23,25],
            'rotation':[1,1]},

            {'name':'Borehole1',
            'pages':[27,29],
            'rotation':[2,2]},

            {'name':'Borehole2',
            'pages':[31,33],
            'rotation':[2,2]},

            {'name':'Borehole3',
            'pages':[35,37],
            'rotation':[2,2]},

            {'name':'Borehole4',
            'pages':[39,41],
            'rotation':[2,2]},

            {'name':'Borehole6',
            'pages':[43,45],
            'rotation':[2,2]},

            {'name':'Borehole7',
            'pages':[47,49],
            'rotation':[2,2]},

            {'name':'Borehole9',
            'pages':[51,53],
            'rotation':[2,2]},

            {'name':'Borehole13',
            'pages':[55,57],
            'rotation':[2,2]},
        ]}

            
             
            

