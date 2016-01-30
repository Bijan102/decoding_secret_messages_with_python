#Import modules
import os

#Create a function called rename_files()
def rename_files():
    #(1) Get file names from a folder
    file_list = os.listdir(r"/Users/bijanfazeli/Desktop/Coding/fun_with_github/Python/decoding_secret_messages_with_python/prank")
    print(file_list)
    #(2) For each file, rename the filename

#Call the rename_files() method
rename_files()
