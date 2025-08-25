#create a password with at least 8 characters, including uppercase, lowercase, digits, and special characters
import random
import string
def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Ensure the password contains at least one of each character type
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest of the password length with random choices from all character types
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = lower + upper + digit + special + ''.join(random.choices(all_characters, k=length - 4))

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)
# Example usage
print("generate strong password: ", generate_password(12))