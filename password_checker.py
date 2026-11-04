import string

# Ask the user to enter a password
password = input("Enter your password: ")

# Check password requirements
if (len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password) and
    any(char in string.punctuation for char in password)):

    print("Your password is STRONG!")

else:
    print("Your password is WEAK!")
