import re
name = input("WHat is your name? ").strip()

matches = re.search(r"^.+, .+$" , name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(name)