with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
    print(len(content))

#Auto closes the file after exiting the with block