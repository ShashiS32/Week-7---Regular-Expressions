import re

email = input("What is your email?: ").strip()

if re.search(r"^\w+@[^0-9]\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
