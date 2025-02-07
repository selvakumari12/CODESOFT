import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),  
        random.choice(string.ascii_lowercase),  
        random.choice(string.digits),       
        random.choice(string.punctuation)      
    ]

    
    password += random.choices(characters, k=length - 4)

    
    random.shuffle(password)

    return ''.join(password)


try:
    password_length = int(input("Enter the desired length of the password (minimum 4): "))
    if password_length < 4:
        print("Password length must be at least 4.")
    else:
        
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid number.")
