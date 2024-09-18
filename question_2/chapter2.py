# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

def separate_and_convert(s):
    """
    Separates a string into numeric and letter substrings, then converts even numbers and upper-case letters
    to their ASCII decimal values.

    Args:
    s (str): The input string containing both numbers and letters.

    Returns:
    tuple: Two lists containing ASCII codes for even numbers and upper-case letters respectively.
    """
    # Separate numbers and letters
    number_string = ''.join(filter(str.isdigit, s))
    letter_string = ''.join(filter(str.isalpha, s))

    # Convert even numbers to ASCII code values
    even_numbers = [int(c) for c in number_string if int(c) % 2 == 0]
    ascii_codes_numbers = [ord(str(num)) for num in even_numbers]

    # Convert upper-case letters to ASCII code values
    upper_case_letters = [c for c in letter_string if c.isupper()]
    ascii_codes_letters = [ord(c) for c in upper_case_letters]

    return ascii_codes_numbers, ascii_codes_letters

# Example usage
if __name__ == "__main__":
    s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
    ascii_codes_numbers, ascii_codes_letters = separate_and_convert(s)
    print("ASCII codes for even numbers:", ascii_codes_numbers)
    print("ASCII codes for upper-case letters:", ascii_codes_letters)
