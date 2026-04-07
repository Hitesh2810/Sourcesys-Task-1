import math  #Inbuilt module for mathematical operations
R="\033[91m"
RA = "\033[0m"
def add(a, b):
    try:
        result = a + b
        print(R + "=====================ADDITION MODULE=======================")
        print(R + f"Square root of result:" + RA, math.sqrt(result))
        return result
    except Exception as e:
        print("Error in addition:", e)