import addition_module
from subtraction_module import subtract
import multiplication_module as mul
from division_module import divide
import mod_module as md
from args import args
import kwargs

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


print(CYAN + "========== CALCULATOR OUTPUT ==========")

a = 10
b = 5
a_m, b_m, r = mul.multiply()

print(GREEN + f"Addition ({a} + {b}) = {addition_module.add(a, b)}") #Passed 2 Global Value
print(YELLOW + f"Subtraction ({a} - 9) = {subtract(a)}")#Passed 1 Global Value and fetched 1 Default Value
print(CYAN + f"Multiplication ({a_m} * {b_m}) = {r}")#Fetched 2 Local Value and 1 Return Value
print(RED + f"Division ({a} / {b}) = {divide(a, b)}")
print(GREEN + f"Modulus (100 % 8) = {md.mod(100, 8)}")#Passed 2 parameters and Fetched Remainder Value
print(YELLOW + f"Maximum = {args(12,23,30,554,5665,60,78,863,912,10)}")#Passed Random Values and Fetched Maximum Value
print(RED + f"Kwargs = {kwargs.Hitesh(word1='My', word2='Self', name='Hitesh S', action='completed', task='task', extra='given', don = 'on', day=6, ai='th', mon='April', year=2026)}")
#Passed Random Key-Value Pairs and Fetched Sentence by Concatenating Values
print(CYAN + "=======================================" )