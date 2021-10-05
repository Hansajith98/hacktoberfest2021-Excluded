import random
name = input("YOUR NAME PLAYER !? ")
diff=str(input("SELECT DIFFICULTY : EASY STANDARD OR HARD \n")) # difficulty level for the player.
print("GOOD LUCK ! ", name)
if diff == 'EASY':
    easy_words=['apple','papaya','orange','banana','kiwi','strawberry','cherry'] # if difficulty is easy, then list of easy words.
    word=random.choice(easy_words)
    print("YOUR WORD IS A FRUIT") # initial hint for the player.
    hint=str(input("DO YOU WANT A HINT ? YES OR NO \n")) # addition hint for the player, which will result in deduction in number of turns.
    if hint == 'YES':
        char=random.choice(word) # if hint is asked for then a random letter from the random word is given to the player.
        print("YOUR WORD HAS",char,"IN THE NAME")
        turns = 5
    else :
        turns = 8

elif diff == 'STANDARD':
    standard_words=['tesla','ferrari','ford','porsche','subaru','jaguar','mclaren'] # list of standard words.
    word=random.choice(standard_words)
    hint=str(input("DO YOU WANT A HINT ? YES OR NO \n"))
    print("YOUR WORD IS THE NAME OF A CAR COMPANY")
    if hint == 'YES':
        char=random.choice(word)
        print("YOUR WORD HAS",char,"IN THE NAME")
        turns = 7
    else :
        turns = 11

elif diff == 'HARD':
    hard_words=['pythagoras','albert enistein','charls darwin','michael faraday','thomas edison','nikola tesla','cv raman'] # list of hard words.
    word=random.choice(hard_words)
    print("YOUR WORD IS THE NAME OF A SCIENTIST")
    hint=str(input("DO YOU WANT A HINT ? YES OR NO \n"))
    if hint == 'YES':
        char=random.choice(word)
        print("YOUR WORD HAS",char,"IN THE NAME")
        turns = 10
    else :
        turns = 13
life = turns # using aditional variable to determine number of mistakes made by the player.
print("GUESS YOUR WORD")
guesses = ''
while turns > 0:
    blanks = 0
    flag = 0
    for i in word: # loop used to iterate each character of the word.
        if hint == "YES":
            if i == char: # if hint is YES then a random letter is printed at it's respective place in the word.
                print(i)
                flag = 1 # flag variable is used to avoide unnecessary blanks.

        if i in guesses: # if guessed letter is in word then printing the same (A)
            print(i)


        else:
            if flag == 1: # to avoide extra blank spaces.
                flag = 0
            else:
                print("_") # to print blank spaces for the word and give an ideal to the player of word length.
                blanks += 1


    if blanks == 0: # condition to determine whether all the characters of the words has been guessed
        print("BRAVO YOU WON WITH,",(life-turns),"MISTAKES ! :)") # number of mistakes along with winning message !
        print("YOUR WORD WAS:",word)
        break
    guess = str(input("GUESS A CHARACTER:")) # input for the used
    if guess == char: # if the entered character is same as the random hint letter then pass
        pass
    else: # if not then append it to guesses (line A)
        guesses += guess # if the guessed character is not in the selected word then decrement the number of turns
        if guess not in word:
            turns -= 1
            print("WORD",guess,"IS NOT PRESENT")
            print("YOU HAVE", + turns, 'MORE GUESSES')
if turns == 0: # if out of turns before guessing the entire word then player lost the game
    print("YOU LOST :( ... ")
