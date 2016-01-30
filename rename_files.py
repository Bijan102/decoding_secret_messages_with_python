#Import modules
import os
import re

#Create a function called rename_files()
def rename_files():
    #(1) Get file names from a folder
    file_list = os.listdir(r"/Users/bijanfazeli/Desktop/Coding/fun_with_github/Python/decoding_secret_messages_with_python/prank")
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"/Users/bijanfazeli/Desktop/Coding/fun_with_github/Python/decoding_secret_messages_with_python/prank")
    #(2) For each file, rename the filename
    for file_name in file_list:
         os.rename(file_name, "".join(i for i in file_name if not i.isdigit()))
    os.chdir(saved_path)
    #(3) Print the renamed files
    file_list.sort()
    print(file_list)
    
#Call the rename_files() method
rename_files()
                  
