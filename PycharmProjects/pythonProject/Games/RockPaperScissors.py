from random import randint


class RockPaperScissors:
    t = ["Rock", "Paper", "Scissors"]

    computer = t[randint(0, 2)]

    player = False

    while not player:

        player = input("Rock Paper Scissors")
        if computer == player:
            print("Tie")

        elif computer == "Rock":
            if player == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You Win!", player, "smashes", computer)
        elif computer == "Paper":
            if player == "Scissors":
                print("You lose!", computer, "covers", player)
            else:
                print("You Win!", player, "smashes", computer)
        elif computer == "Scissors":
            if player == "Rock":
                print("You lose!", computer, "covers", player)
            else:
                print("You Win!", player, "smashes", computer)
        else:
            print("That's not a valid play. Check your spelling!")
        player = False
        computer = t[randint(0, 2)]
