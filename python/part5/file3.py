# modes
# r           reading  default
# w           writing,truncates file first (clear then write /overwrite)
# x          creates new & open for writing
# a          writing, appends at end
# b          binary mode                 like CNN , audio,video files
# t           text mode [default]
# +           open disk file for update(r & w)


# we can create new file using w if file not exist 
# but using x if file exist it will give error but w can overwrite file

# open("sample.txt","rt") # reading and text mode

# see differace bw  r+  w+ a+ mode


f =  open("sample.txt","r+")

f.write("123") 
print(f.read())  # read after text of pointer .... r+ w+ a+ change the pointers

f.close()


