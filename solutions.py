## Questions..

"""
1. How do you distinguish between shutil.copy() and shutil.copytree()?
2. What function is used to rename files??
3. What is the difference between the delete functions in the send2trash and shutil modules?
4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile 
method is equivalent to File objects’ open() method?
5. Create a programme that searches a folder tree for files with a certain file extension 
(such as .pdfor .jpg). Copy these files from whatever location they are in to a new folder.

"""

##  Answers...

"""
1. The shutil.copy() function is used to copy a single file from one location to another, while
 shutil.copytree() is used to copy an entire directory tree from one location to another.

 ------------------------------------------------------------------------------------------


2. The os.rename() function is used to rename files in Python.

------------------------------------------------------------------------------------------


3. The delete functions in the send2trash module move files to the operating system's trash or
 recycle bin, while the delete functions in the shutil module permanently delete files.

 ------------------------------------------------------------------------------------------


4. The equivalent ZipFile method to File objects' open() method is the ZipFile() constructor,
 which is used to create a new ZipFile object and open a ZIP file for reading or writing.

 ------------------------------------------------------------------------------------------

5.

import os
import shutil


folder_path = '/path/to/folder'

destination_folder = '/path/to/destination/folder'

file_extension = '.pdf'


for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        
        if filename.endswith(file_extension):
            
            file_path = os.path.join(foldername, filename)
            
            shutil.copy(file_path, destination_folder)



"""