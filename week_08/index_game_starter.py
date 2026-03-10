import random

def main():
    
    # create new non-empty list called names
    names = 

    # add a new name to the end of the list
    

    # look up the length of the list and assign to num_names
    

    # This is just like in Khansole Academy...
    # prompt the user for an answer, check if it is correct
    # Here's how to do it in a loop!

    # set neutral value for sentinel variable 
    keep_going = 'y'

    # continue game until sentinel variable matches stop value
    while str.lower(keep_going[0]) != 'n':
        print()

        # loop over list to print out each value
        for name in names:
            print(name)

        # use randint to select a valid "index" 
        idx = random.randint(num_names * -1, num_names - 1)

        # get the item at the chosen index
        correct_answer = names[idx]

        # get user's answer
        answer = input(f'Who is in index {idx}? ')
        
        # check user's answer and print appropriate response
        if str.lower(answer) == str.lower(correct_answer):
            print('Good job')
        else:
            print(f'Correct answer was {correct_answer}')
        
        # Ask if user wants to keep going, check against stop value
        keep_going = input("Play again? y/n: ")

    print("bye bye")

if __name__ == '__main__':
    main()