import random

#create a list of the three choices:
rpslist = ["rock", "paper", "scissors"]
shuffled_list = random.shuffle(rpslist)


def check_user_input(choice_one):
    while True:
        if choice_one in rpslist:
            break
        else:
            choice_one = input("Please enter a valid choice: ").lower()

def create_comp_choice(comp_choice):
    comp_choice = shuffled_list[0]
    return comp_choice
    
def check_correct_answer(user_pick,comp_pick,user_score):
    if user_pick == comp_pick:
        user_score += 1
        return user_score


def main():
    #get user input
    user_choice = input("What would you like to throw?: ").lower()

    #create a variable for the score
    score = 0

    #verify it is a valid input
    check_user_input(user_choice)

    #create computer's choice
    correct_choice = create_comp_choice(correct_choice)

    #check if computer's choice is same as user's
    check_correct_answer


main()
