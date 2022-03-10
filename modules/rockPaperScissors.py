# Prompts the user to enter a value: R, P or S
#The program should convert this value into Rock, Paper, or Scissors respectively
# Asks the computer to generate a random value between 0 and 2
# Convert the computer’s choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
# Compare the user’s choice with the computer’s choice to display a message indicating whether
#the user won, lost or drew against the computer
# Showcase what you have learned about conditional statements and create your own functions
import rps

again = 'Y'
while again == 'Y':
    user = rps.user_choice()
    comp = rps.computer_choice()
    rps.check_winner(user, comp)
    again = input('Again? Y/N ')






