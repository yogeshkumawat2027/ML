#Product store

#Design & create an online store for Products(name,price).
#Track total products being created.
#Create a static method to calculate discount on each product based on a % parameter

class Product:
    count = 0

    def __init__(self, name,price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price,percentage):
        final_price = price - (percentage*price/100)
        print(f"Discounted price = {final_price}")

p1 = Product("phone",10_000)
p2 = Product("laptop", 10)
p3 = Product("pen" , 10)

p1.get_info()
Product.get_count()
p1.calc_discount(10000,12)
        