import os
import shutil

path = "copy.txt"
path2 = "emptyfolder"
try:
    #os.remove(path)
    #os.rmdir(path2) #rmdir = remove directory
    shutil.rmtree(path2) #dangerous, can delete a folder with its contents
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete this folder using this function")
else:
    print(f"{path2} was deleted")
