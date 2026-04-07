import random  #Generates random numbers
Y = "\033[93m"
RA = "\033[0m"  
def multiply(a, b):
    try:
        print(Y + "==================MULTIPLICATION MODULE===================")
        c=random.randint(1, 10)
        d=random.randint(10, 50)
        print(Y + f"Multiplication of random Number {c} and {d} :" + RA, c * d)
        return a * b
    
    except Exception as e:
        print("Error in multiplication:", e)