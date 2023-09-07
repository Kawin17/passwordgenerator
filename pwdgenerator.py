import random
import string


def generate_password(length, complexity):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    if complexity == 'low':
        chars = lowercase + numbers
    elif complexity == 'medium':
        chars = lowercase + uppercase + numbers
    else:
        chars = lowercase + uppercase + numbers + symbols

    password = ''.join(random.choice(chars) for i in range(length))
    return password


length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity level (low, medium, high): ")
password = generate_password(length, complexity)
print("Your generated password is:", password)




