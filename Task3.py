# Codsof
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Password length must be greater than 0.")
                continue
            password = generate_password(password_length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid password length (a positive integer).")

if __name__ == "__main__":
    main()
