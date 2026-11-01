# Methods 
# 1. instance method --> 1st parameter should self , can access class attributes
 #2. class method  --> 1st parameter = cls , access only class attributes, decorator(it can change behaviour) @classmethod       
 # 3.static method --> not need any specific parameter , cannot access instance attribute    and class attributes , use decorator @staticmethod                                              
class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM, storage):
        self.RAM = RAM
        self.storage = storage
    def get_info(self):       #instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"Discounted price = {final_price}")
        
l1 = Laptop("16gb" , "512gb")
l2 = Laptop("8gb","256gb")
l1.get_info()
Laptop.get_storage_type()
l1.calc_discount(40_000,10)



