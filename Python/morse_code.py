morse_code = {
                    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 
                    'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..'
                }

def english_to_morse():
    '''
    Translate a letter/word/phrase from english to the morse code equivalent. Prints a list of each
    character in its morse code dot and dash form using Python.
    '''
    your_string = input('Enter string to translate to morse code:\n')
    your_string = your_string.upper()

    # creates empty list to append morse code keys to
    translated_string = []

    print('\ntranslating,....translating,....*bing*\n')

    # loops through each character in the user string
    for char in your_string:
        # loops through each key in the dictionary for each character in the string
        for item in morse_code:
            # if the character matches the dictionary key
            if item[0] == char:
                # appends that value to the translated list
                translated_string.append(morse_code[item])

    # prints the final translation
    print('Your code for each character in morse is:\n')
    print(translated_string)
