import os

folders = input("Please provide list of folder names with space seperated: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Please provide valid foldername. {folder} folder does not exist.")
        break
    except PermissionError:
        print("No access to folder:" + folder)
        break
    
    print("======= Listing the folder : " + folder)
    
    for file in files:
        print(file)