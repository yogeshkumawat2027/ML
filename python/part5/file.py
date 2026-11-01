#file -- open, operations(read,write,append),close ,delete


#file operations
 #1.open      f= open("data.txt" , "r")  r-> read mode ex: r-read , w-write
 #                        ^
#                         |
#                     filename/path

f = open("sample.txt","r")  #file object

# data = f.read()
# print(data, type(data))

print("########")

print(f.readline())    #read line by line
print(f.readline())

f.close()    #always for protect to unexpected changes