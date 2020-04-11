# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:42:04 2019

@author: MaxFelius

TOOLBOX

function to automatically create latex and csv tables
Also flexibel to add and remove rows

TODO
    -finish script
    -automatically copy the output table to clipboard
    
TODO Class
    -finish empty function
    -move contents on self.Print() to self.Create() and let the rest call
    self.Create()
    -Add additional function to the latex script (centering, label, caption,
    first column with text)
"""
import numpy as np

class CreateTable(object):
    '''This will be an object that creates a table and can print/write the table 
    to the desired format. The formats that are going to be implemented (for now)
    are csv and latex'''
    
    def __init__(self,header,headerC,*row):
        '''The input for this object should all be lists'''
        
        #Check if input is a list
        assert type(header) == list
        
        self.row = list(row)
        self.header = header
        self.headerC = headerC
        
    def __str__(self):
        '''This method will print the current object in csv format'''
        return self.Print('CSV')
    
    def Header():
        pass
    
    def HeaderC():
        pass
    
    def DeleteRow():
        pass
    
    def NewRow():
        pass
    
    def Options():
        pass
    
    def Create(extension):
        if extension == 'Latex' or extension == 'latex':
            pass
        elif extension == 'csv' or extension == 'CSV':
            pass
        else:
            print('Please select the type of table you want to copy (Latex or CSV).')

    def Write(self,extension):
        if extension == 'Latex' or extension == 'latex':
            pass
        elif extension == 'csv' or extension == 'CSV':
            pass
        else:
            print('Please select the type of table you want to copy (Latex or CSV).')

    def Copy(self,extension):
        if extension == 'Latex' or extension == 'latex':
            pass
        elif extension == 'csv' or extension == 'CSV':
            pass
        else:
            print('Please select the type of table you want to copy (Latex or CSV).')
    
    def Print(self,extension):
        if extension == 'Latex' or extension == 'latex':
            output_object = '\\begin{table}[h!]\n'
            output_object = output_object + '\\begin{tabular}'
            numCol = np.shape(self.row)[1]
            
            output_object = output_object + '{'+'l'*numCol+'}\n\n'
            
            #header
            for index,item in enumerate(self.header):
                if index == len(self.header)-1:
                    output_object = output_object + str(item) + '\\\ \n'
                else:
                    output_object = output_object + str(item) + ' & '
            
            output_object = output_object + '\hline\n'
            
            #body
            dim = np.shape(self.row)
            
            for rows in range(dim[0]):                            
                for index,item in enumerate(self.row[rows]):
                    if index == len(self.row[rows])-1:
                        output_object = output_object + str(item) + '\\\ \n'
                    else:
                        output_object = output_object + str(item) + ' & '            
            
            output_object = output_object + '\\end{tabular}\n'
            output_object = output_object + '\\end{table}\n'
            
            return output_object
            
        elif extension == 'csv' or extension == 'CSV':
            output_object = '#'
            
            #header
            for index,item in enumerate(self.header):
                if index == len(self.header)-1:
                    output_object = output_object + str(item) + '\n'
                else:
                    output_object = output_object + str(item) + ','
            
            #body
            dim = np.shape(self.row)
            
            for rows in range(dim[0]):                            
                for index,item in enumerate(self.row[rows]):
                    if index == len(self.row[rows])-1:
                        output_object = output_object + str(item) + '\n'
                    else:
                        output_object = output_object + str(item) + ','
            
        else:
            print('Please select the type of table you want to copy (Latex or CSV).')        
            
        return output_object
        
def CreateLatexTable(name,*rows):
    LatexTable =[] #output
    
    start = 'nothing'
    
    return LatexTable

def _test():
    header = ['bike','car']
    row1 = [1,2]
    row2 = [3,4]
    row3 = [5,6]
    obj = CreateTable(header,None,row1,row2,row3)
    
#    print(obj)
    
    print(obj.Print('latex'))
    
if __name__ == '__main__':
    _test()
