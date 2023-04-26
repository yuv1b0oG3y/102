import shutil
import os

from_dir = "/Users/ninenine/Downloads"
to_dir = "/Users/ninenine/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".pdf"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "pdf_files"
        path3 = to_dir + "/" + "pdf_files" + "/" + filename
        #print("path1", path1)
        #print("path3", path3)
        if os.path.exists(path2):
            print("MOVING" + filename + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("MOVING" + filename + "...")
            shutil.move(path1, path3)