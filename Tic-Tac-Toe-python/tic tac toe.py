import random


print('''                                                                                                   
 ######   ######     ####            ######     ##       ####            ######     ###    ####### 
   ##       ##      ##  ##             ##       ##      ##  ##             ##      ## ##   ##      
   ##       ##     ##                  ##      ####    ##                  ##     ##   ##  ##      
   ##       ##     ##                  ##      ## #    ##                  ##     ##   ##  #####   
   ##       ##     ##                  ##     ######   ##                  ##     ##   ##  ##      
   ##       ##      ##  ##             ##     ##   #    ##  ##             ##      ## ##   ##      
   ##     ######     ####              ##    ###   ##    ####              ##       ###    ####### 
                                                                                                   
                                                                                                   
''')
print("WELCOME TO TIC TAC TOE \n")
player_choice = input("X or O :::  \n").upper()
pc_choice = ""

if player_choice == "X":
    pc_choice = "O"
else:
    pc_choice = "X"

print(f"player_choice = {player_choice} \n")
print(f"pc_choice = {pc_choice} \n")

Tabel = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

print(f"{Tabel[1]} | {Tabel[2]} | {Tabel[3]}  \n"
      f"{Tabel[4]} | {Tabel[5]} | {Tabel[6]}  \n"
      f"{Tabel[7]} | {Tabel[8]} | {Tabel[9]}  \n")

game_is_on = True
RCL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while game_is_on:
    choice = input("Tabel number ??? :")
    Tabel[int(choice)] = player_choice

    RCL.remove(int(choice))
    random_choice = random.choice(RCL)
    RCL.remove(int(random_choice))
    print(f"Computer chose = {random_choice}")
    Tabel[int(random_choice)] = pc_choice
    print(f"{Tabel[1]} | {Tabel[2]} | {Tabel[3]}  \n"
          f"{Tabel[4]} | {Tabel[5]} | {Tabel[6]}  \n"
          f"{Tabel[7]} | {Tabel[8]} | {Tabel[9]}  \n")
    if Tabel[1] == Tabel[2] == Tabel[3] != ".":
        print(f"winner is {Tabel[1]}")
        game_is_on = False
    elif Tabel[4] == Tabel[5] == Tabel[6] != ".":
        print(f"winner is {Tabel[4]}")
        game_is_on = False
    elif Tabel[7] == Tabel[8] == Tabel[9] != ".":
        print(f"winner is {Tabel[7]}")
        game_is_on = False
    if Tabel[1] == Tabel[5] == Tabel[9] != ".":
        print(f"winner is {Tabel[1]}")
        game_is_on = False
    if Tabel[3] == Tabel[5] == Tabel[7] != ".":
        print(f"winner is {Tabel[3]}")
        game_is_on = False
    if Tabel[1] == Tabel[4] == Tabel[7] != ".":
        print(f"winner is {Tabel[1]}")
        game_is_on = False
    if Tabel[2] == Tabel[5] == Tabel[8] != ".":
        print(f"winner is {Tabel[2]}")
        game_is_on = False
    if Tabel[3] == Tabel[6] == Tabel[9] != ".":
        print(f"winner is {Tabel[3]}")
        game_is_on = False


print('''                                                                                  
   ####     ##     ##   ##  #######             ###    ##   ##  #######  ######  
  ##  ##    ##     ##   ##  ##                 ## ##   ##   ##  ##       ##   ## 
 ##        ####    ### ###  ##                ##   ##  ##   ##  ##       ##   ## 
 ##        ## #    ## # ##  #####             ##   ##   ## ##   #####    ######  
 ##  ###  ######   ## # ##  ##                ##   ##   ## ##   ##       ## ##   
  ##  ##  ##   #   ##   ##  ##                 ## ##     ###    ##       ##  ##  
   ##### ###   ##  ##   ##  #######             ###      ###    #######  ##   ## 
                                                                                 
                                                                                 
''')