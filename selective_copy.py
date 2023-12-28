import shutil
import os


def selective_copy():
    extension = input("What extension would you like to look for?\n")
    path_to_search = input("Enter the path\n")
    destination = os.path.join(path_to_search, f"{extension}_files/")

    for folder_name, sub_folders, file_names in os.walk(path_to_search):
        for name in file_names:
            if name.endswith(f'.{extension}'):
                source = os.path.join(path_to_search, name)
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.copy(source, destination)

selective_copy()
