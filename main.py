email = input("What is your email?: ").strip()

user, domain = email.split("@")

if user and "." in domain:
    pre_dot, post_dot = domain.split(".")
    if pre_dot and post_dot:
        print("Valid")
    else:
        print("Invalid")