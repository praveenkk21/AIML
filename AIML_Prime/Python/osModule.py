import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("The file does not exist")