import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    choices = {'player': {player_choice}, 'computer': {computer_choice}}
    return choices
choices = get_choices()
print(choices)

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors'):
        return "Rock smashes scissors! You win!"
    elif (player == 'paper' and computer == 'rock'):
        return "Paper covers rock! You lose."
    elif (player == 'scissors' and computer == 'paper'):
        return "Scissors cuts paper! You win!"
    else:
        return "Invalid choice. Please choose rock, paper, or scissors."

choice = get_choices()
result = check_win(choice['player'], choice['computer'])

print(result)

