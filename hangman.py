import requests
import random



word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
random_word = random.choice(WORDS).decode('utf-8')
display = []
lives = 6
for word in random_word:
    display += "_"
print("""          _______  _        _______  _______  _______  _       
|\     /|(  ___  )( (    /|(  ____ \(       )(  ___  )( (    /|
| )   ( || (   ) ||  \  ( || (    \/| () () || (   ) ||  \  ( |
| (___) || (___) ||   \ | || |      | || || || (___) ||   \ | |
|  ___  ||  ___  || (\ \) || | ____ | |(_)| ||  ___  || (\ \) |
| (   ) || (   ) || | \   || | \_  )| |   | || (   ) || | \   |
| )   ( || )   ( || )  \  || (___) || )   ( || )   ( || )  \  |
|/     \||/     \||/    )_)(_______)|/     \||/     \||/    )_)
                                                               """)

while True:
    print(random_word)
    gameDisplay = " ".join(display)
    guess = input("Guess the word, enter a letter: ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        lives -= 1
        print(f"Lost a life. {lives} lives remaining")
        if lives == 0:
            print("Lost all lives.")
            print("You lose.")
            break

    gameDisplay = " ".join(display)
    pcDisplay = "".join(display)
    print(gameDisplay)

    if pcDisplay == random_word:
        print("You win.")
        break
