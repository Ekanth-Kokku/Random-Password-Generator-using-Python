import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: Please say at least one yes to generate your password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_bool_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['yes']:
            return True
        elif choice in ['no']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def get_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Hello,Welcome to the Password Generator!")

    length = get_int_input("Enter the length of your password: ", 1, 100)
    print("I need some information from you to generate your password.Say (yes/no)")
    use_letters = get_bool_input("Do you need to include letters in your password?: ")
    use_numbers = get_bool_input("Do you need to include numbers in your password?: ")
    use_symbols = get_bool_input("Do you need to include symbols in your password?: ")

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Your unique password is:", password)
        print("Thank you")

if __name__ == "__main__":
    main()
