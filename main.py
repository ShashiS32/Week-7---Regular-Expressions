import re

email = input("What is your email?: ").strip()

if re.search(r"^\w+@[^0-9]\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
