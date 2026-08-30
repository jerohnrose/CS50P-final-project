import math
import secrets
import string

def main():
    print("Welcome to password toolkit!!!")
    print("Note: 'Predictability' measures how hard your password is to guess.")
    print("Higher bits = harder to crack. Below ~28 bits is weak, 60+ is strong.\n")
    # menu loop, calls the functions below based on user choice
    while True:
            user = input("Choose an option ('Checker', 'Generator', or 'Quit'): ").strip().lower()

            if user == "checker":
                password = input("Enter password: ")
                rating = check_strength(password)
                entropy = calculate_entropy(password)
                is_common = is_common_password(password)
                entropy_label = describe_entropy(entropy, is_common)
                print(f"Strength: {rating}")
                print(f"Predictability: {entropy:.1f} bits ({entropy_label})")
            elif user == "generator":
                length = get_length()
                use_symbols = ask_include_symbols()
                password = generate_password(length, use_symbols)
                print(f"Password: {password}")
            elif user == "quit":
                break
            else:
                print("Invalid option, please try again.")



def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename) as file:
            return {line.strip().lower() for line in file if line.strip()}
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Common password check disabled.")
        return set()

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def check_strength(password):
    if is_common_password(password):
        print("This password appears in a list of commonly used passwords.")
        return "Weak"

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    variety_score = has_upper + has_lower + has_digit + has_symbol

    if len(password) < 8:
        return "Weak | Password must have atleast 8 characters"
    elif len(password) >= 12 and variety_score == 4:
        return "Very Strong"
    elif len(password) >= 8 and variety_score >= 3:
        return "Strong"
    elif variety_score == 2:
        return "Fair | Variety score too low"
    else:
        return "Weak"

def calculate_entropy(password):
    pool_size = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if has_upper:
        pool_size += 26
    if has_lower:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_symbol:
        pool_size += 32

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return entropy

def describe_entropy(entropy, is_common):
    if is_common:
        return "Very Predictable"
    if entropy < 28:
        return "Very Predictable"
    elif entropy < 36:
        return "Predictable"
    elif entropy < 60:
        return "Somewhat Unpredictable"
    elif entropy < 128:
        return "Unpredictable"
    else:
        return "Highly Unpredictable"

def get_length():
    while True:
        length_input = input("Choose length of password: ")
        try:
            length = int(length_input)
            if length < 4:
                print("Length must be at least 4.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")

def ask_include_symbols():
    while True:
        use_symbols = input("Do you want to include symbols (y/n)? ").lower().strip()
        if use_symbols == 'y':
            return True
        elif use_symbols == 'n':
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def generate_password(length = 12, use_symbols = True):
    # returns a randomly generated password string using secrets.choice()
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password


COMMON_PASSWORDS = load_common_passwords()


if __name__=="__main__":
    main()

