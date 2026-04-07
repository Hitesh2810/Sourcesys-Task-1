def divide(a, b=1):  # Setting default value of b to 1 to avoid division by zero
    C= "\033[94m"
    try:
        print(C + "=======================DIVISION MODULE=======================")
        return a / b
    except ZeroDivisionError:
        print(C + "=======================================================")
        print(C + "Cannot divide by zero")
    except Exception as e:
        print("Error in division:", e)