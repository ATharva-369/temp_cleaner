import os
path = input("enter the path of the temp folder you want to clean: ")
if os.path.exists(path):
    files = os.listdir(path)
    for i in files:
        i = os.path.join(path,i)
        os.remove(i)
        print("the temp folder is cleaned :)")
        print("-------------------------------------------")
else:
    print("are u sure this directory exists -_-")        