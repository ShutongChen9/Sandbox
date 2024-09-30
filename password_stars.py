MINIMUM_LENGTH = 6

password = input(f"Enter your password (at least {MINIMUM_LENGTH}): ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid")
    password = input(f"Enter your password (at least {MINIMUM_LENGTH}): ")
print("*" * len(password))