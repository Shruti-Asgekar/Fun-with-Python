import random
def winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

player_score = 0
computer_score = 0

while True:
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    win = winner(player_choice, computer_choice)
    if win == "player":
        player_score += 1
        print("You win this round!")
    elif win == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("It's a tie!")

    print(f"Score - You: {player_score}, Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")