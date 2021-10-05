import requests


word = input("Enter a word: ")
api = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(api).json()[0]['meanings']

for i in response:
    print(f'Parts of Speech: {i["partOfSpeech"].title()}')
    for definition in i["definitions"]:
        print(f"Definition: {definition['definition'].capitalize()}")
        if len(definition["synonyms"]):
            print(f"Synonyms: {', '.join(definition['synonyms']).title()}")
        print(f"Example: {str(definition.get('example')).capitalize()}")

input()
