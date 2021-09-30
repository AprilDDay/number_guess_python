import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score. So try to make a score that's unbeatable!")
    else:
        print("The current high score is {} attempts.".format(min(attempts_list)))
