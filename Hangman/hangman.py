import random
chance = 7
words = ["ant", "baboon","badger", "bat"," bear", "beaver", "camel", "cat"," clam", "cobra", "cougar",
         "coyote","crow","deer", "dog", "donkey", "duck","eagle","ferret", "fox" ,"frog"," goat "]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman =6
word_choice = random.choice(words)
word_list = []
selection = []
final = []



for i in word_choice:
    word_list.append(i)

print("THE WORD HAS BEEN CHOSEN")

for i in range(len(word_list)):
    final.append("_")

for i in range(1):
    x = random .choice(word_list)
    selection.append(x)

for i in range(len(word_list)):
    if selection[0] == word_list[i]:
        final[i] = selection[0]


print(final)

case =len(word_list)
check =0
while chance>=0:
    chance = chance-1

    player_choice = input("GUESS THE LETTER")
    player_choice = player_choice.lower()
    for i in range(len(word_list)):
        if player_choice == word_list[i]:
            final[i] = player_choice
            case =1

    if case!=1:
        print(HANGMANPICS[hangman])
        print(final)
        print(f"CHANCES LEFT :{chance}")
        hangman =hangman-1
        if chance ==0:
            print("U LOST :")
            print("WORD IS:")
            print(word_choice)
            exit()
    else:
        print(final)

    if word_list == final:
        chance=-1
    case= 0



print("U WON THE WORD IS:")

print(word_choice)


