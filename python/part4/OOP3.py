#Encapsulation
print("#############  Encapsulation ############ ")
class BankAccount:
    def __init__(self,name,balance):
        self.name = name  #public
       # self._balance = balance  # protected but in python its accesable outside the class
        self.__balance = balance  # private

    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self,newBalance): #setter
        self.__balance = newBalance

acc1 = BankAccount("Rajat", 10000)

acc1.set_balance(20000)
print(acc1.name , acc1.get_balance())

print(acc1.name , acc1._BankAccount__balance)  ## balance access through this method in python



print("######### Inheritance ########")

class Employee:
    start_time = "10AM"
    end_time = "6PM"

class Teacher(Employee) :
    def __init__(self,subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary ,role):
        super().__init__(role)
        self.salary = salary

        

t1 = Teacher("Math")

print(t1.subject, t1.start_time,t1.end_time)

acc1 = Accountant(25_000,"CA")
print(acc1.role,acc1.salary,acc1.start_time)

#Multiple inheritance ---> notes

print("########### Abstraction ########")  #Rewatch or read in notes or gpt
        


#Polymorphism ---> 1. function overriding 2. Duck Typing
print(1+2 ,"hello"+"world")  #operator overloading

#1. function overriding --> in inheritance same function into parent and child class
                          # or redefining parent class fnx in child class
                          #Example : in notes

#2. Duck typing --> same function name into non-related class

class Dog:
 def speak(self):
  print("Bark")
  
class Cat:
 def speak(self):
   print("Meow")
