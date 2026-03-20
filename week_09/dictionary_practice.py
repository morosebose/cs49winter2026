"""
dictionary_practice.py

Exercise for working with creating, modifying, accessing 
elements in, and iterating over a dictionary

Programmer: Surajit A. Bose, Date: 20251201
"""
def main():
    # Create a dictionary of state capitals
    state_caps = { 'Oregon' : 'Salem',
        'Idaho' : 'Boise',
        'Hawaii' : 'Honolulu',
        'Alaska' : 'Juneau' }

    # Add key : value pairs 
    state_caps['Maryland'] = 'Annapolis'
    state_caps['Kentucky'] = 'Lexington'

    # Access a value using bracket notation
    wrong_ky_cap = state_caps['Kentucky']
    print(wrong_ky_cap)

    # Oops! Change the value for Kentucky to be correct
    state_caps['Kentucky'] = 'Frankfort'
    ky_cap = state_caps['Kentucky']
    print(ky_cap)

    # Non-existent key will result in a KeyError!
    # ca_cap = state_caps['California']

    # Check for the existence of a key
    print('California' in state_caps)       # False
    print('Hawaii' in state_caps)           # True

    # Check for the existence of a value
    print('Boise' in state_caps.values())   # True
    print('Olympia' in state_caps.values()) # False

    # Iterate over all key : value pairs
    for state, city in state_caps.items():
        print(f'The capital of {state} is {city}')

    # Iterate over keys
    for state in state_caps:
        print(state)
    
    # Iterate over values
    for city in state_caps.values():
        print(city)


if __name__ == "__main__":
    main()