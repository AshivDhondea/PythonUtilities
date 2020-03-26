# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:25:03 2020

Renaming files and copying them to a different directory.

Particularly useful when these files will be included in a LaTeX document later on.
(Since LaTeX does not allow you to import files with underscores or spaces in the
file name)

@author: Ashiv Hans Dhondea

Reference:
https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python

"""
import glob
import shutil

directory_name = "Original Images";
file_extension = "jpg";

new_directory_name = "Renamed Images";
str_to_remove = "_";
str_replacement = "";

for file in glob.glob(directory_name+"/*."+file_extension):
    index_for_filename = file.index('\\');
    filename =  file[index_for_filename+1:];
    new_filename = filename.replace(str_to_remove,str_replacement);
    shutil.copy2(directory_name+"/"+filename,new_directory_name+"/"+new_filename);
    
