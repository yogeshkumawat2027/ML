# List Comprehensions

# [output for item in iterable if condition]

# example 0 to 5 squares [0,1,,4,9,16,25]

squares = []
for i in range(6):
    squares.append(i*i)

print(squares)

#List Comprehensions is easy and precise way to do these type of tasks

sq = [i*i for i in range(6)] # [output iterable condition]
print(sq)

#store squres for only odd num
sqr = [i*i for i in range(6) if i%2 != 0]
print(sqr)

#negative numbers replace to zero(0) [-2,-4,3,5,-1] to [0,0,3,5,2,0]

nums = [-2,-3,3,4,-1,7]

nums = [0 if val < 0 else val for val in nums]
print(nums)

# uppercase on words

words = ["hello","python","apnacollege"]

words = [val.upper() for val in words]
print(words)

# [0, 1, 4, 9, 16, 25]
# [0, 1, 4, 9, 16, 25]
# [1, 9, 25]
# [0, 0, 3, 4, 0, 7]
# ['HELLO', 'PYTHON', 'APNACOLLEGE']