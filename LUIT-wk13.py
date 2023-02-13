#!/usr/bin/env python3.7

#Import os & stat module
import os
import stat

#Create an empty list
files_list = []

#Set the CWD as a variable
my_path = os.getcwd()

#Create list of files in CWD
dir_list = os.listdir(my_path)


#Set variables for dictionary
for file in dir_list:
    status = os.stat(file)
    permissions = stat.filemode(status.st_mode)
    file_path = os.path.join(my_path, file)
    file_size = os.stat(file_path)
    

    #Create a dictionary
    my_dictionary = {
        'File Permissions' : permissions,
        'Path' : file_path,
        'File Name' : file,
        'File Size' : file_size.st_size
    }
    files_list.append(my_dictionary)

    print(my_dictionary)
