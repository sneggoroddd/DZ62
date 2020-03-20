from filemanager import  copy_file_or_directory, filenames, author_info, quit
import shutil
import os
import sys

def test_copy_file_or_directory():
    name = "test_filemanager.py"
    new_name = "test1"
    def copy_file_or_directory(name, new_name):
        return
    assert  new_name in os.listdir()
os.rmdir(new_name)



