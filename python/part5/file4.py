
import os

#file --> open file with --> automatic close  file after tasks

with open("sample.txt","r") as f:
    print(f.read())

    #Delete file import os module

os.remove("sample2.txt")