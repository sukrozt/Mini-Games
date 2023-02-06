import random as rd
actions = ["rock", "paper", "scissors"]
score_1 = 0
score_2 = 0
round_counter = 0
round_num = int(input("How many rounds you eant to play?: "))
while True:
    round_counter += 1
    print("Round", round_counter)
    player_1 = rd.choice(actions)
    player_2 = rd.choice(actions)
    print("Player 1:", player_1, "Player 2:", player_2)
    if player_1 == player_2:
        print("Tie! Both players chose the same action.")
    else:
        if player_1 == "scissors":
            if player_2 == "rock":
              print("Player 2 wins!")
              score_2 += 1
            else:
              print("Player 1 wins!")
              score_1 += 1
        elif player_1 == "rock":
            if player_2 == "paper":
              print("Player 2 wins!")
              score_2 += 1
            else:
              print("Player 1 wins!")
              score_1 += 1
        elif player_1 == "paper":
            if player_2 == "scissors":
              print("Player 2 wins!")
              score_2 += 1
            else:
              print("Player 1 wins!")
              score_1 += 1

    winner_score = max(score_1, score_2)
    print(f"The score of the winner is: {winner_score}")
    if round_counter == round_num:
        break

if score_2 > score_1:
    print("The winner is Player 2!")
elif score_2 < score_1:
    print("The winner is Player 1!")
else:
    print("It's a draw!")