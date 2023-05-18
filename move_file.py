import os
import shutil

from_dir = "Downloads"
to_dir = "Document"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    file_name_without_ext, file_ext = os.path.splitext(file_name)
    print("File Name: ", file_name_without_ext)
    print("File Extension:", file_ext)
    print("---")

