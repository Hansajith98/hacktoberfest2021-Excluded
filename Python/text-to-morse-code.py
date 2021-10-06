#TODO: Assignment: Text to Morse Code Converter

print("\nWelcome to TEXT to MORSE code Converter")

morse_list = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",

    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "-----",
    "......."
]

char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

should_continue = True

while should_continue:
    convert_type = input('\nPress to convert:\n1 - Text to Morse code.\n2 - Morse code to Text.\n3 - Exit\n')

    if convert_type == '1':
        text = input("Enter the text: ").upper()
        morse_code = ''
        for char in text:
            index = char_list.index(char)
            morse_code += f'{morse_list[index]} '
        print(f'Morse code: {morse_code}')

    elif convert_type == '2':
        morse_code = input('Enter the Morse code: ')
        text = ''
        code = morse_code.split(' ')
        for char in code:
            text += char_list[morse_list.index(char)]
        print(f'Text: {text}')

    else:
        should_continue = False

