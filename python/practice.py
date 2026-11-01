
# a = 10.0
# c = "10.0"
# b = int(a)
# print(type(b+a),a==c)

# color = input("Enter color :")

# if color == "Red" :
#     print("Stop")
# elif color == "Yellow" :
#     print("look")
# elif color == "Green" :
#     print("Go")
# else : print("Enter valid color")

# age = int (input("Enter age :"))

# if (age < 13) : print("child")
# elif (age >= 13 and age< 18) : print("teenager")
# else : print("adult")

# i = 1

# while i<=10 :
#     print(i)
#     i += 1


# for i in range(5,0,-1):
#     print(i)



# list1 = [1,2,3,4]

# print(list1[0:4:2])

# list1.append(5)



# print(len(list1))

# list1[0] = 10

# for l1 in list1 :
#     print(l1)


# t1 = (1,2,3,4,5)

# t1[0] = 10   //error tuple cannot change
# print(t1[0])


import numpy as np # Create & Output an array 
# arr = np.array([1, 2, 3, "Prime" , 4, 5]) 

# arr3 = np.array([[1, 2, 3], [4, 5, 6], [4, 5, 6]])

# print(type(arr3), arr3.shape)

# print(type(arr), arr)

arr = np.array([1, 2, 3, 4, 5, 6]) 

reshaped = arr.reshape((3,2)) # converts (1x6) => (2x3)

print(reshaped, reshaped.shape)