"""
hi_lo.py

Play specified number of rounds of guessing game:
- Assign a random number between 1 and 100 inclusive to user and to computer
- Ask user to guess whether user number is higher or lower than computer number 
- If user is correct, user scores a point

Programmer: Surajit A. Bose, Date: May 22, 2025
"""

# import statements
import random

# constants
NUM_ROUNDS = 5

def main():
    """Assign user and computer numbers, get user guess, keep score, print results"""
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Set initial score to zero
    score = 0
    for i in range(NUM_ROUNDS):
    
        # Create and assign random numbers to computer and user
        comp_num = random.randint(1, 100)
        user_num = random.randint(1, 100)
        
        # Ensure the two numbers aren't equal, since "equal" is not an allowed guess
        while user_num == comp_num:
            user_num = random.randint(1, 100)

        # Display user's number
        print(f"Your number is {user_num}")

        # Get guess of higher or lower from user and convert to all lowercase
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
            
        # Extension 1: Safeguard user input
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ").lower()
        
        # Main program logic! Check if user's guess is correct
        if user_num > comp_num and choice == "higher" \
        or user_num < comp_num and choice == "lower":
        # If it is correct, augment score and print happy message
            score += 1
            print(f"You were right! The computer's number was {comp_num}")
        # Otherwise, print sad message
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}")
        print()
        
    # Extension 2: Conditional ending messages
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
        
    # To pass autograder, comment out above if-elif-else and uncomment next line
    # print("Thanks for playing!")
    
    print()

if __name__ == "__main__":
    main()