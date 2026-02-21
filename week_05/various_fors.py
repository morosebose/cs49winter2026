"""
various_fors.py

Demonstrate the different ranges in for loops.

Programmer: Surajit A. Bose, Date: May 23, 2025
"""

def main():
    
    # print the first 10 even numbers
    for i in range(10):             # implicitly this is range(0, 10, 1)
        print(i * 2)                # Use the 'i' value inside the for-loop
    print()
    
    # print the first 10 positive integers
    # loop does not execute once i reaches or goes beyond 11
    for i in range (1, 11):      # specify start and stop; step is implicitly 1
        print(i)
    print()
    
    # print the first 10 odd numbers
    # loop does not execute once i reaches or goes beyond 20
    for i in range(1, 20, 2):   # specify start, stop, and step
        print(i)
    print()
    
    # print with a decreasing value of i
    # i starts at 5, decreases by 1 until it reaches 0
    for i in range(5, 0, -1):
        if i > 1:
            print(f"I have {i} marbles left. Oops, there goes another!")
        else:
            print(f"I'm down to my last marble. Oops, there it goes!")
    print("I haven't any marbles left. I've lost every one!")
    
    print()
   
if __name__ == "__main__":
    main()