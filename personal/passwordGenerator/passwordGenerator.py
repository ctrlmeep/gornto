import random
import string

def generate_password(length):
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice("!@#$%^&*_+-=")
    ]

    character_pool = (string.ascii_letters * 3) + (string.digits * 5) + "!@#$%^&*_+-="
    for i in range(length - 3):
        password.append(random.choice(character_pool))

    random.shuffle(password)
    password = "".join(password)

    return password

if __name__ == '__main__':
    print("Password: " + generate_password(int(input("Enter password length: "))))
