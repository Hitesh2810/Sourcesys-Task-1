import re

phone = "9876543210"

pattern = r"^[0-9]{10}$"

if re.match(pattern, phone):
    print("Valid Lead Phone")
else:
    print("Invalid Phone")