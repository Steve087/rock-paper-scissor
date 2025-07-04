import random

emojis = {
    'r': '🪨',
    's': '✂️',
    'p': '📃'
}

choices = ['r', 'p', 's']
while True:
    count = 0
    for _ in range(3):
        user_choice = input('rock, paper, or scissors?(r/p/s)').lower()
        if user_choice not in choices:
            print('invalid choice')
            continue

        computer_choice = random.choice(choices)
        print(f"you chose {emojis[user_choice]}")
        print(f"computer chose {emojis[computer_choice]}")
        if user_choice == computer_choice:
            print("its a draw")
        elif (user_choice == 'r' and computer_choice == 's') or \
                (user_choice == 'p' and computer_choice == 'r') or \
                (user_choice == 's' and computer_choice == 'p'):
            print("you won this round")
            count += 1
        else:
            count -=1
            print("computer won this round")

    if count >0:
            print('you won')
    elif count==0:
            print('its a draw')
    else :
        print('you loose')

    should_continue = input('Do you want to play again? (y/n): ').lower()
    if should_continue != 'y':
            print("Thanks for playing!")
            break



