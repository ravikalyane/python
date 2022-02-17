import random
import string

# ask user the length of password
length = int(input("Enter length of password: "))

characters = string.ascii_letters + string.punctuation + string.digits
random_characters = [random.choice(characters) for i in range(length)]
password = ''.join(random_characters)
print(password)