# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

def decrypt_message(ciphertext, shift):
    """
    Decrypts a given ciphered message using a Caesar cipher with the specified shift value.

    Args:
    ciphertext (str): The ciphered message.
    shift (int): The number of positions to shift in the Caesar cipher.

    Returns:
    str: The decrypted message.
    """
    decrypted_message = []
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            new_char = chr((ord(char) - start - shift_amount) % 26 + start)
            decrypted_message.append(new_char)
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Example usage
if __name__ == "__main__":
    ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
    for s in range(1, 26):
        decrypted = decrypt_message(ciphertext, s)
        print(f"Shift {s}: {decrypted}")
