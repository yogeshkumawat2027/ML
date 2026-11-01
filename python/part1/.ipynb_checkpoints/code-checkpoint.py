# name = input("Enter name :")
# age = input("enter age : ")
# print("Hello " , name , "you are ", age , "year old")

# print(type(name))

# print(10+3*2**2)

 ###########

# a =11

# if(a==10): print("yes")
   
# else :
#    print("no")
#    print("no")

#########


# count = 1
# num=int(input("enter number"))

# while(count<=10):
#     print(count*num)
#     count+=1


########


string = "hello"

# for var in string:
#     print(var)

# if('o' in string):
#     print("o exists")


# range(n) ---> 0 to n-1
#range(start,stop,step)   step---> increment or updation 
 #  start by default ----> 0
 #step by default -----> +1


# for i in range(5):
#     print(i)  # 0 1 2 3 4
#     print(i+1)  # 1 2 3 4 5


# for i in range(1,10,2):
#     print(i)           #13579


# sum of n natural numbers

# sum = 0
# n = int(input("enter number : "))
# for i in range(1,n+1):
#     sum+=i
# print(sum)


#function

# def hello():             #fnx definition 
#     print("hello")

# hello()     #fnx call
# hello()


# def sum(a,b):
#     return a+b

# print(sum(2,3))



#Lambda Function        ---> used for expressions

# sum = lambda a,b: a+b
# print(sum(4,5))

def factorial(n):
    sum = 1

    for i in range(n,0,-1):
       sum *= i
    return sum 

  
print(factorial(5))















