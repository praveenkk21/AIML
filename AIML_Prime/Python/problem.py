#find where pythion exists on sample2.txt


with open("sample2.txt", "r") as f:
    line=1
    data=f.readline()
    while(data):
        data=f.readline()
        print(data)
        if "python" in data:
            print(f"Found in the line {line}")
            break
        line+=1


with open("sample2.txt", "r") as f:
    lineNumber = 0
    for line in f:
        lineNumber += 1
        if "python" in line:
            print(f"Found in the line {lineNumber}")
            break
        