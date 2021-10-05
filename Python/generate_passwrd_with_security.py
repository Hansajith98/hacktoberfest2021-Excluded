import secrets
import string

def createAlphabet(lowercase=True, uppercase=True, digits=True, symbols=True, whitespace=False) -> str:
    alphabet = ''

    if lowercase:
        alphabet += string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if symbols:
        alphabet += string.punctuation
    if whitespace:
        alphabet += ' '

    return alphabet

def createPassword(alphabet: str, size=12) -> str:
    return ''.join(secrets.choice(alphabet) for x in range(size))

if __name__ == "__main__":
    alphabet = createAlphabet()
    password = createPassword(alphabet, size=15)

    print(password)
