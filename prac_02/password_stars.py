# password_stars.py
# Program to check password length and print asterisks
def get_password(min_length):
    """Get password from user with error checking."""
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    """Print asterisks matching password length."""
    print("*" * len(password))

def main():
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

main()