#Practice Problem

#find word exist or not and in which line
line =1
with open("sample.txt","r") as f:

    data = True
    while data :
        data = f.readline()

        if("Python" in data):
            print(f"Word found in line {line}")
            break
        line += 1
    