# Exception Handling 

# try, except, else , finally 

# exeption -- x= input ans = 10/input and input =0 

# try :
#    -------
#    -------
# except zeroDivisionError(or custom error):
#    ----
#    ----
# else :     (if no any error occur)

try: 
    x = int(input("Enter x :"))
    ans = 10/x

except ZeroDivisionError:                 #checkout built-in exceptions
    print("Divide by 0 is not allowed")

except ValueError:
    print("Invalid input") # for txt string

else: 
    print(f"ans = {ans}")

finally:   # exception occur or not it will execute (always)
    print("End of program")