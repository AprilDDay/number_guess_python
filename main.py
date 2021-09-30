import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score. So try to make a score that's unbeatable!")
    else:
        print("The current high score is {} attempts.".format(min(attempts_list)))

def start_game():
    random_num = int(random.randint(1,100))
    print("Hello Young Jedi! Welcome to the game of guesses!")
    player_name = input("What's your name?")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes / No)").format(player_name)
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try: 
            guess = input("Pick a number between 1 and 100")
            if int(guess) < 1 or int(guess) > 100:
                raise ValueError("Please guess a number between 1 and 100...really...")
            if int(guess) == random_num:
                print("Nice! You got it! Way to go!")
                attempt +=1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No)")
                attempts = 0
                show_score()
                random_num = int(random.randint(1, 100))
                if play_again.lower() == "no":
                    print("Cool! Be on your way!")
                    break
            elif int(guess) > random_num:
                print("Guess again...lower...")
                attempts +=1
            elif int(guess) < random_num:
                print("Guess again...higher this time...")
                attempts += 1
        except ValueError as err:
                print("Oh no! Try to guess a number between 1 and 100...")
        else: 
            print("That's cool! Be on your way!")
if __name__ == '__main__':
    start_game()