from random import randint
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str= ", ".join(choices)
    action_user = input(f"Entre un choix {choices_str}: ")
    action_user = int(action_user)
    action = Action(action_user)
    return action
def get_computer_selection():
    selection = randint(0, len(Action)-1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    print("------------------------------------------------")
    print(f"Choix Joueur: {user_action.name}")
    print(f"Choix Ordinateur: {computer_action.name}")
    print("------------------------------------------------")
    if user_action == computer_action:
        print("Choix identique. match null !")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock brise Scissors! Vous gagnez.")
        else:
            print("Peper enveloppe Rock! Vous perdez.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors decoupe Paper! Vous gagnez.")
        else:
            print("Rock brise Scissors! Vous perdez.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper enveloppe Rock! Vous gagnez.")
        else:
            print("Scissors decoupe Paper! Vous perdez.")
def main():
    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action)-1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue
        computer_action = get_computer_selection()
        determine_winner(user_action , computer_action)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

if __name__ == '__main__':
    main()

