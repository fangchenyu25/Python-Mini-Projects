# collect user preferences
# - length 
# - should contain uppercase
# - should contain special
# - should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string 

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() 
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 8:
        print("Password length must be at least 8 characters.")
        return None
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    if not all_characters:
        print("Error: No character types selected.")
        return None
    
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
        
    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range (remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)

    str_password = "".join(password)
    return f"Generated password: {str_password}" if str_password else "Error: Unable to generate password."

password = generate_password()
print(password)


