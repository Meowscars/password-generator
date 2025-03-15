import random

characters = ["12345678900", "qwertyuiopasdfghjklzxcvbnm", ".@#-_"]

def password(length: int):
    password = []
    for _ in range(length-2):
        password += [random.choice(characters[1])]
    
    password.insert(random.randrange(0, length-2), random.choice(characters[0]))
    password.insert(random.randrange(0, length-2), random.choice(characters[2]))

    return "".join(password)

if __name__ == "__main__":
    print(password(8))