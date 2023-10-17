import random
import string

def generate_password(length=12):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Ensure the password length is at least 6 characters
    length = max(length, 6)
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main program
if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the length of the password (minimum 6 characters): "))
            if password_length >= 6:
                break
            else:
                print("Password length should be at least 6 characters.")
        except ValueError:
            print("Please enter a valid number for password length.")

    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
