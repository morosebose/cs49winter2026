def main():
    # Create a list called `fruit_list` that contains the following fruits: 
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print(len(fruit_list))
    
    # Add 'mango' at the end of the list. 
    fruit_list.append('mango')
    
    # Print the value at the end of the list to check that 'mango' was correctly added
    print(fruit_list[-1])

    # Check if 'honeydew' is in the list.
    # if it is, replace it with 'melon'
    # if it is not, add 'melon' to the second position in the list.
    if 'honeydew' in fruit_list:
        ind = fruit_list(honeydew)
        fruit_list[ind] = 'melon'
    else:
        fruit_list.insert(1, 'melon')
        
    print() # blank line just for ease of reading the console

    # Print the updated list one fruit at a time.
    for fruit in fruit_list:
        print(fruit)

    print() # blank line just for ease of reading the console

    # Print the entire list on one line
    print(fruit_list)
    
if __name__ == '__main__':
    main()