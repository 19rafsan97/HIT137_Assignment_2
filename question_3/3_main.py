# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

def decrypt(text, key):
    """
    Decrypts the given text encrypted with a Caesar cipher using the specified key.

    Args:
    text (str): The encrypted text.
    key (int): The number of positions each letter was shifted.

    Returns:
    str: The decrypted text.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def process_numbers(tybony_inevnoyr):
    """
    Process numbers based on the input value.

    Args:
    tybony_inevnoyr (int): The number to process.

    Returns:
    list: Processed list of numbers.
    """
    ahzoref = [1, 2, 3, 4, 5]
    
    while tybony_inevnoyr > 0:
        if tybony_inevnoyr % 2:  # Check if the number is odd
            ahzoref.remove(tybony_inevnoyr)  # Remove the number from the list
        tybony_inevnoyr -= 1  # Decrement the number
    
    return ahzoref

# Example of usage
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  # Define a set
result = process_numbers(tybony_inevnoyr=5)  # Process numbers

def update_dictionary():
    """
    Updates a dictionary with a new value.

    Returns:
    dict: Updated dictionary.
    """
    ybpny_inevnoyr = 10
    zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
    zl_qvpg['xrl4'] = ybpny_inevnoyr
    return zl_qvpg

# Example of usage
dictionary = update_dictionary()

def check_value(dictionary):
    """
    Checks the value against certain conditions and prints messages accordingly.
    
    Args:
    dictionary (dict): The dictionary to check for values.
    """
    tybony_inevnoyr = 100
    tybony_inevnoyr += 10

    for v in range(5):
        print(v)
        v += 1
    
    if not zl_frg == {1, 2, 3, 4, 5} and dictionary['xrl4'] == 10:
        print("Condition met!")
    
    if 5 not in dictionary:  # Use 'dictionary' instead of 'zl_qvpg'
        print("5 not found in the dictionary!")
    
    print(tybony_inevnoyr)
    print(dictionary)
    print(zl_frg)

# Example of usage
check_value(dictionary)
