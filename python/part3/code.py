word1 = "hello"
word2 = "word"

#concatination
print(word1+word2)

print(word1[0])


for ch in word1 :
    print(ch)


#strings in python immutable .... 
# why we can not chnage character value ex: word[3] = 'H'  we can not replace

print(len(word1))  # length of string

#normal formating

a=5
b=10
sum = a+b

print("language is {}".format("pyhton"))
print("sum of {} & {} is {}".format(a,b,sum))  # sum of 5 & 10 is 15

#index based formating

print("sum of {1} & {0} is {2}".format(a,b,sum))  # sum of 10 & 5 is 15

#f-string

print(f"sum of {a} & {b} id {a+b}")

##################################################

# Lists  ---> mutable sequence of valuse  like as array

marks = [99,98,95,91,72]

print(marks)
print(len(marks))

marks[4] = 90

print(marks)

data = [40,"abc", 100.99]
print(type(data))

## slicing ---> notes

#methods
# 1 num.append(val)   --> add one element at the end
# 2 num.insert(idx , val)  --> insert at idx

#3 I.sort()  --> "arranges in increasing order"

# I.reverse()   -> revrse order

nums = [1,2,3]

nums.append(4)
print(nums)  # [1, 2, 3, 4]

# we wants [1, 2,10, 3, 4]  2nd index par 10

nums.insert(2,10)

print(nums)

print("sorting")
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)


for val in nums:
    print(val)
  
idx = 0
for val in nums:
    if(val==4):
        print(idx)
        break
    else:
        idx+=1


#Tuples ---> immutable sequence of values  --- we can not change the value 

tup = (1,2,3,4,5,"abc", 4.5)
print(tup)
print(type(tup))  #<class 'tuple'>

# tup[2] = 10
# print(tup[2])        #  File "D:\Prime-AIML\python\part3\code.py", line 100, in <module>
                     # tup[2] = 10
                     # TypeError: 'tuple' object does not support item assignment

tup2 = (1) #expression 
tup4 = ("abc") #expression
tup3 = (1,) #tupple 


print(type(tup2))   #<class 'int'> treat as expression not tuples for single value in 
print(type(tup3))  # <class 'tuple'> after comma
print(type(tup4))   #<class 'str'>

#methods

#1. t.index(val)  --> returns 1st occurance idx
#2. t.count(val)  --> counts total occurance

tupp = (1,2,2,3,2,4,5)
print(tupp.index(2))  #1
print(tupp.count(2))   #3


##########  Dictionary   ####### like as object

print("Dictionary --> Key:value pairs")

info = {
    "name" : "john",
    "cgpa" : 9.2,
    "subjects" : ["math" , "science"],
    3.14 : "PI"
}
print(info)
print(type(info))   # <class 'dict'>

print(info["name"])
print(info[3.14])

info["cgpa"] = 9.8  #mutable 
print(info["cgpa"])

# Dictionary --> mutable, unordered

# Dictionary methods 
#1.  d.keys()     --> returns all keys
#2.  d.values()  --> returns all values
#3.  d.items()   --> returns(key,val) pairs
#4.  d.get(key)   --> return value  why if info[key] ---- because if key not exist info[key] will give error but .get(key) gives none
#5. d.update({key : val})  --> add new item


dict_keys = list(info.keys())
dict_values = list(info.values())
print(dict_keys)
print(dict_values)


######### Sets --> Collection of unique elements  #####

# Sets --> mutable ,unordered but elements --> immutable

# set = { 1,2,2,2,2}  --> {1,2} length = 2 because unique elements

print("Sets")
s = {1,2,2,3} 
print(s)       # {1, 2, 3}
print(type(s))

s.add(5)
print(s) 

empty_set = {}
print(type(empty_set))  # dictionary not set

# empty_set = set()  <--- set

#  ### set methods ###

# s.add(val)
#s.remove(val)
#s.clear()      #empties the set
# s.pop()       removes a random val
 # s.union(set2)     returns new union  (all) s is set1
 # s.intersection(set2)  returns new intersaction (common elements)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
print(s1.union(s2))
print(s1.intersection(s2))










