import re

email = input("What is your email?: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-z]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
