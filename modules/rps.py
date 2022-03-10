import random


def user_choice():
    user_selection = ''
    while user_selection not in ('R', 'P', 'S'):
        user_selection = input('Enter choice(R/P/S):')
    if user_selection == 'R':
        print('You chose rock')
    elif user_selection == 'P':
        print('You chose paper')
    elif user_selection == 'S':
        print('You chose scissors')
    return user_selection


def computer_choice():
    choice = random.choice(range(0, 3))
    if choice == 0:
        print('Computer chose rock')
        choice = 'R'
    elif choice == 1:
        print('Computer chose paper')
        choice = 'P'
    elif choice == 2:
        print('Computer chose scissors')
        choice = 'S'
    return choice


def check_winner(user_selection, choice):
    if user_selection == choice:
        print('Tie!')

    elif user_selection == 'R':
        if choice == 'P':
            print('Paper wins! Computer wins!')
        else:
            print('Rock wins! You win!')

    elif user_selection == 'P':
        if choice == 'S':
            print('Scissors win! Computer wins!')
        else:
            print('Paper wins! You win!')

    elif user_selection == 'S':
        if choice == 'R':
            print('Rock wins!Computer wins!')
        else:
            print('Scissors wins!')

    else:
        print('Other')


if __name__ == '__main__':
    print("hello from rps")