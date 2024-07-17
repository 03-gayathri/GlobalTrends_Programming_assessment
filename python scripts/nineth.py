'''code to create a Python function that generates a random password. The password should 
contain a mix of uppercase letters, lowercase letters, digits, and special characters'''
import random
import string
def generate_random_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)
password = generate_random_password(16)
print(f"Generated password: {password}")

