import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """Generates a random password based on given criteria."""
    
    if not (use_uppercase or use_lowercase or use_numbers or use_special):
        raise ValueError("At least one character type must be selected")
    
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)
