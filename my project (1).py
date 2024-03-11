# number scrabble game is a two players game take turns to take a number from a list
# then the first who has a sum of 15 of any 3 numbers in his list who is the winner .

import itertools
print("Welcome to Number scrabble game!")

player_1_list = []
player_2_list = []
list_of_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(list_of_choices) > 0:
    print("Player 1: It is your turn")
    while True:
        try:
            player_1_choice = int(input("Please select a number from 1 to 9: "))
            if player_1_choice not in list_of_choices:
                print("Error! Please insert a valid choice")
                continue
            break
        except ValueError:
            print("Error! Please enter a valid integer")

    player_1_list.append(player_1_choice)
    list_of_choices.remove(player_1_choice)
    print("Now the list of player 1 is:", player_1_list)
    print("Remaining choices:", list_of_choices)

    for combination in itertools.combinations(player_1_list, 3):
        if sum(combination) == 15:
            print("Player 1 is the winner!")
            exit()

    if len(list_of_choices) == 0:
        print("It is a draw!")
        exit()

    print("Player 2: It is your turn")
    while True:
        try:
            player_2_choice = int(input("Please select a number from the list of choices: "))
            if player_2_choice not in list_of_choices:
                print("Error! Please insert a valid choice")
                continue
            break
        except ValueError:
            print("Error! Please enter a valid integer")

    player_2_list.append(player_2_choice)
    list_of_choices.remove(player_2_choice)
    print("Now the list of player 2 is:", player_2_list)
    print("Remaining choices:", list_of_choices)

    for combination in itertools.combinations(player_2_list, 3):
        if sum(combination) == 15:
            print("Player 2 is the winner!")
            exit()

    if len(list_of_choices) == 0:
        print("It is a draw!")
        exit()



