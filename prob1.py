#prob1.py
#Anne Smith
#ITSC203

#-	Count of files found in subdirectory
import os
import hashlib
import shutil
from pathlib import *
from prettytable import PrettyTable

def multi(files):
    cell = ""
    for i in files:
        cell += (i + "\n")
        #print(cell)
    return cell
    
x = PrettyTable()
x.field_names = ["Directory", "Filename", "Hash (SHA256", "File_Count"]
hexFiles = []
directory = os.getcwd()
subfolders = [x[0] for x in os.walk(directory)]
index = 0
for folders in subfolders:
    files = [f for f in os.listdir(subfolders[index]) if os.path.isfile(os.path.join(subfolders[index], f))]
    lst1=[hashlib.sha256(i.encode()).hexdigest().upper() for i in files]
    hexFiles.append(lst1)
    file_count = len(files)
    x.add_row([subfolders[index], multi(files), multi(lst1), file_count])
    index += 1
print(x, end =' ')

'''
PART2 hash value and change file for its hash
'''
newDir = subfolders[-1]
copy_path = os.chdir(newDir)
index = 0

for folders in subfolders:
    path = subfolders[index]

    for f in os.listdir(path):
        # Path to the original file
        original_file_path = os.path.join(path, f)
        # Only operate on files
        if os.path.isfile(original_file_path):
            # Get file name portion only
            file_name = os.path.basename(original_file_path)
            str = hashlib.sha256(file_name.encode('utf-8'))
            text_hashed = str.hexdigest()
            # Get the extension of the file and create a path for it             
            # change extension to hash and then add .extension                                                   
            extension = f.split(".")[-1]
            extension_path = os.path.join(newDir, extension)
            new_name = text_hashed +'.'+ extension
            # Create the path for files with the extension if it doesn't exist
            if not os.path.exists(extension_path):
                os.makedirs(extension_path)

            # Copy the files into the new directory
            shutil.copyfile(original_file_path, os.path.join(extension_path, new_name))
    index +=1
