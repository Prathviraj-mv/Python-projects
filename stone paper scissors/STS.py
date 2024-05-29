import random

print('''                                                                                                                                                                         
                            ##                                                                                                                                          
 ######   ######   ######   ##                ######    #####   ######   ######   ######            ######   ######   ######   ######   ######   ######   ######   ######  
 ##  ##   ##  ##   ##  ##   ## ###            ##  ##       ##   ##  ##   ##  ##   ##  ##            ##       ##  ##     ##     ##       ##       ##  ##   ##  ##   ##      
 ##       ##  ##   ##       ####              ##  ##   ######   ##  ##   ######   ##                ######   ##         ##     ######   ######   ##  ##   ######   ######  
 ##       ##  ##   ##  ##   ## ##             ######   ##  ##   ######   ##       ##                    ##   ##  ##     ##         ##       ##   ##  ##   ## ##        ##  
 ##       ######   ######   ##  ##            ##       ######   ##       #####    ##                ######   ######   ######   ######   ######   ######   ##   #   ######  
                                              ##                ##                                                                                                         
''')
rock1 = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper1 = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors1 = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

choice_list = [rock1, scissors1, paper1]
computer_choice = random.choice(choice_list)
game_is_on = True
while game_is_on:
    player_choice = input("ROCK ,PAPER,SCISSORS>>???").lower()

    if player_choice == "rock":
        player_choice = rock1

    if player_choice == "paper":
        player_choice = paper1

    if player_choice == "scissors":
        player_choice = scissors1

    winner = ""

    print(f"computer choice = {computer_choice} VS \n player choice = {player_choice}")

    if player_choice == rock1 and computer_choice == paper1:
        winner += "U LOST"
    if player_choice == scissors1 and computer_choice == rock1:
        winner += "U LOST"
    if player_choice == paper1 and computer_choice == scissors1:
        winner += "U LOST"

    if player_choice == paper1 and computer_choice == rock1:
        winner += "U WIN"
    if player_choice == rock1 and computer_choice == scissors1:
        winner += "U WIN"
    if player_choice == scissors1 and computer_choice == paper1:
        winner += "U WIN"

    if player_choice == computer_choice:
        print("DRAW")
    print(f"{winner} ")
