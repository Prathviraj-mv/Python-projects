import random
print('''
.-. . . .-. .-. .-.   .-. . . .-.   . . . . .  . .-. .-. .-. 
|.. | | |-  `-. `-.    |  |-| |-    |\| | | |\/| |(  |-  |(  
`-' `-' `-' `-' `-'    '  ' ` `-'   ' ` `-' '  ` `-' `-' ' ' 
                                                             
''')
number = random.randint(0,1000)

chance_used = 0
game_is_on = True
print("THE COMPUTER HAS CHOSEN THE NUMBER")
while game_is_on:
    user_input = input("Enter the number  ")
    user_input = int(user_input)
    if user_input > number:
        print("UR IN FRONT OF THE NUMBER")
    if user_input < number:
        print("UR BEHIND THE NUMBER")
    if user_input == number:
        print(f'u guessed it the number is  {number} ')
        game_is_on = False
    chance_used +=1
    print(f"chance_used = {chance_used} ")

