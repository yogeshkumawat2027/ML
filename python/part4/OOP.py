

#OOP --- >  maping real world objects 

#class --> blue print of an object(instance of class)

class Student:
    subject = "Python"
    college = "abc"

st1 = Student()
print(st1)    # <__main__.Student object at 0x0000024B80CD86E0>   <----- memory address

print(st1.subject ,st1.college) #Python abc


#COnstructor --> fnx which we can create object

# __init__ method  <--- constructor  , initialize our object

def __init__(self):
    print("This is the constructor")   # self --> current instance of the class


####### 
print("########")

class Student2:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self) :
        return self.cgpa

stu1 = Student2("Urvashi",9.0)
stu2 = Student2("Kunal",8.5)

print(stu1.name , stu2.name)
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

# in python --> single constructor in a class

#class attribute --> blong to class (common)
#instance attribute  --> blong to object(like name , sub)

class Student3:
    college_name = "ABC" #class -attribute
    pi = 3.1

    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        self.pi = 3.14

stu = Student3("rajat",9.2)

print(stu.name)
print(Student3.college_name)
print(stu.college_name)
# print(Student3.name)  # error
print(stu.pi) #3.14 because instance attribute has high priority







