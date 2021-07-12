#!/usr/bin/python3

''' 

AMZY-0 (M.Amin Azimi .K) 
Copyright (C) (2019-2020-2021)  AMZY-0 (M.Amin Azimi .K) 

"Luxarg" (This program) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import io
import os
from posixpath import abspath, expanduser
from sys import float_repr_style
from tkinter import messagebox
from os import path
from os import getenv
from typing import final

from PIL.Image import new

def message(path_msg, text_msg):


    if text_msg == 'saved !':
        msg = messagebox.showinfo('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))
    
    else:
        msg = messagebox.showerror('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))


# def writer(path_and_filename, text, widget_destroy):
    
#     # path_and_filename equal to EMPTY 
#     if path_and_filename == '':
#         path_and_filename = '''Field is empty !
# Please HIT <F2> and enter your file name again ...'''
#         message(path_and_filename, '')

#     # if is directory :
#     elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
#         # if not a file 
#         message(path_and_filename, ': Is directory')   

#     elif path_and_filename[:2] == '~/':
#         path_and_filename = path_and_filename.replace('~/','%s/'% 
#         str(getenv('HOME'))).strip()
    
#         try:
#             fin = open(path_and_filename, 'w')
#             fin.write(text)
#             message(path_and_filename, 'saved !')
            
#             fin.close()
        
#         except OSError as error :
#             message(path_and_filename, str(error)[10:])
    


    
#     # relational path for home directory added (~)  
#     elif path_and_filename == '~':
#             message(path_and_filename, ': Is directory')

#     else:
        
#         try:
#             fin = open(path_and_filename, 'w')
#             fin.write(text)
#             message(path_and_filename, 'saved !')
            
#             fin.close()
        
#         except OSError as error :
#             message(path_and_filename, str(error)[10:])
    

#     return widget_destroy.destroy()

####################################################
# IO 
####################################################
# Input and Output UNIT 
def io_luxarg(path_and_filename, text, io_mode, text_field, file_path):
    
    # if ~/<*>.<txt/py/c/cpp/...>
    path_and_filename = path_and_filename.replace('~/', '%s/' % str(getenv('HOME').strip()))
        
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = 'Field is empty ...!'
        message(path_and_filename, '')
    

    elif path_and_filename == '~':
        message(path_and_filename, ': Is directory (Directory is not readable)')   

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory (Directory is not readable)') 
    


    elif io_mode == 'r':
        # delete all the buffer and after open file 
        text_field.delete('1.0', 'end')



        try:
            fin = open(path_and_filename, io_mode)
            readed =  fin.read()
            text_field.insert('1.0', str(readed))
            text_field.configure(state='disabled')
            fin.close()

        except FileNotFoundError as error:
            message('', str(error)[10:])

        except OSError as error:
                    message('', str(error)[10:])

        
        text_field.configure(state='disabled')
    
    # relational path for home
    elif io_mode=='w':
        path_and_filename = path_and_filename.replace('~/','%s/'% 
        str(getenv('HOME'))).strip()
        
        try:
            fin = open(path_and_filename, io_mode)
            fin.write(text)
            message(path_and_filename, 'saved !')
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])

    file_path.bind('<Escape>', lambda e : text_field.focus())
    file_path.delete(0, 'end')
    return text_field.focus()
    
