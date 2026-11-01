info = [
    ("Alice","Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob","Math"),
    ("Alice" , "English"),
    ("Charlie", "English")
]




# -- list all unique course 

unique_courses = set()   # empty set 

for name,course in  info:
   print(name,course)

print("########")

for tup in info:
   unique_courses.add(tup[1])

for val in unique_courses :
   print(val)

print("########")

#list all students enrolled in English

english_students = set() 
for tup in info:
   if(tup[1]=="English"):
      english_students.add(tup[0])

for val in english_students :
   print(val)

print("########")

# create a dictionary (student , set of courses)  -- see maa'm method

students = set()
for tup in info:
   students.add(tup[0])

dic = {}

for student in students:
   courses = set()
   for tup in info:
      if(tup[0]==student):
         courses.add(tup[1])
   dic.update({student:courses})  

print(dic)

# mam's method 

print("########")

dict = {}

for name,course in info:
   if(dict.get(name)==None):
      dict.update({name : set()})
      dict[name].add(course)
   else :
      dict[name].add(course)

print(dict)
