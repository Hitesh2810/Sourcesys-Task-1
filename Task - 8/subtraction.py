import datetime  #Inbuilt module for handling date and time operations
G = "\033[92m"
RA = "\033[0m"
def subtract(a, b):
    try:
        print(G + "====================SUBTRACTION MODULE======================")
        print(G + "Operation time Of Subtraction:", datetime.datetime.now()) #Prints the current date and time of the operation
        return a - b
    except Exception as e:
        print("Error in subtraction:", e)