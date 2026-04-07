import addition
from subtraction import subtract
import multiplication as mul
import division
R="\033[91m"
G="\033[92m"
Y="\033[93m"
C="\033[94m"
RA="\033[0m"

def main():
    try:
        print("=======================================================")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print(R + f"Addition:" + RA , addition.add(a, b))
        print(G + f"Subtraction:" + RA, subtract(a, b))
        print(Y + f"Multiplication:"+ RA, mul.multiply(a, b))
        print(C + f"Division:" + RA, division.divide(a, b))

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()