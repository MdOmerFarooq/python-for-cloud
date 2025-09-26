import os   # os module lets us to talk with os and perform certain actions on os

# function to return files or error message on given path 

def List_folder_path(folder_path):   
    try :
        files = os.listdir(folder_path)  # os.listdir() method is used to list directory on given path 
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"


folder_paths = input('Enter the dir paths followed by space :').split()

for folder_path in folder_paths :
    files , error_message = List_folder_path(folder_path)
    if files:
        print(f'Files in {folder_path} are : ')
        for i in files:
            print(i)
    else :
        print(f"{error_message} : for folder_path")
    