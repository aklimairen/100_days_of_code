# Choosing a random number between 1 and 100
import random
import art

# global Constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# a function to check user's guess against the actual answer
# track the number of turns and reduce by 1 if they get it wrong


def check_answer(guess, answer, turns):
    """
   Checks answer against gusse and returns the number of turns remaining
  """
    if guess > answer:
        print('too high')
        return turns - 1
    elif guess < answer:
        print('too low')
        return turns - 1
    else:
        print(f'You got it, the answer was {answer}')


def set_difficulty():
    level = input('Choose a difficulty. Type "easy" Or  "hard":')
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)
    print('Welcome to the Number Guessing Game')
    print('I am thinking of a number between 1 and 100')
    answer = random.randint(1, 100)
    print(f"The actual answer is {answer}")
    # make a function to define difficulty
    turns = set_difficulty()
    # repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f'You have {turns} remaining to guess the number')
        # let the user guess a number
        guess = int(input("Guess a Number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('Sorry !! You are out of turns')
            return
        elif guess != answer:
            print('guess again')


game()
