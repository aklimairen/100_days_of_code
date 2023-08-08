from art import logo, vs
from game_data import data
import random


def formate_data(account):
    """Takes the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_descr} from {account_country}'


def check_answer(guss, a_followers, b_followers):
    """Take the user guss and follower count and return if they got it right"""
    if a_followers > b_followers:
        return guss == "a"
    else:
        return guss == "b"


# Design Art
print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
# make the game repeatable
while game_should_continue:
    # Generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print(f"compare-A: {formate_data(account_a)}")
    print(vs)
    print(f"Against compare-B: {formate_data(account_b)}")

    # Ask user to guss
    guss = input("who has more followers? Type A or B:").lower()
    # Check if a user is correct
    # Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guss, a_follower_count, b_follower_count)
    # Give user feedback on their guss
    # score keeping
    if is_correct:
        score += 1
        print(f"you are right and current score is {score}")
    else:
        print(f'Sorry you are wrong and current score is {score}')
        game_should_continue = False

