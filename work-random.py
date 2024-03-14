import random
import time

def clear_line():
    print('\r' + 'Rock    ', end='\r')
    time.sleep(0.5) 
    print('\r' + 'Rock Paper    ', end='\r')
    time.sleep(0.5) 
    print('\r' + 'Rock Paper Scissors    ', end='\r')
    time.sleep(0.5) 
    print('\r' + 'Rock Paper Scissors Shoot   ', end='\r')
    time.sleep(0.5) 

def main():
    options = [
        ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """, 'rock'),
        ("""
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """, 'paper'), 
        ("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """, 'scissors')
    ]

    return random.choice(options)

def ask():
    option = main()
    answer = input("What do you have(don't lie, I can see you 😉): ").lower()
    
    print(option[0])
    print(answer)

    if answer == option[1]:
        print(f"Both players selected {answer}. It's a tie!")
    elif answer == "rock":
        if option[1] == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif answer == "paper":
        if option[1] == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif answer == "scissors":
        if option[1] == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

clear_line()
ask()
