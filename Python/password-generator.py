import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'O', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']


password = []
new_sym = [password.append(symbols[random.randint(0, 8)]) for i in range(0, 2)]
new_num = [password.append(numbers[random.randint(0, 9)]) for i in range(0, 3)]
new_num = [password.append(alphabet[random.randint(0, 50)]) for i in range(0, 5)]

random.shuffle(password)
def list_string(password):
    string = ""
    for i in password:
        string += i
    return string
if __name__ == "__main__":
    print(f"Here is your 10 digt random password: {list_string(password)}")