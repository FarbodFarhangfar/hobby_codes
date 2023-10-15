import random
import string


def generate_password(length, include_lower=True, include_upper=True, include_numbers=True, include_special=True):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    # Create the character pool based on the chosen options
    character_pool = ""
    if include_lower:
        character_pool += lowercase_letters
    if include_upper:
        character_pool += uppercase_letters
    if include_numbers:
        character_pool += numbers
    if include_special:
        character_pool += special_characters

    # Check if at least one character set is selected
    if not character_pool:
        raise ValueError("At least one character set must be included.")

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


# Example usage:
length = 25
include_lower = True
include_upper = True
include_numbers = True
include_special = True

password = generate_password(length, include_lower, include_upper, include_numbers, include_special)
print(password)
