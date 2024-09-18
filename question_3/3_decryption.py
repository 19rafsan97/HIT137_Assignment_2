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

# Example decryption with a guessed key
key = 13  # This key value needs to be determined
encrypted_code = """
tybony inevnoyr  = 100 
z1_qvpg = ('xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3') 

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr 
    ybpny inevnoyr = 5 
    ahzoref= [1, 2, 3, 4, 5] 
    
    juvyr ybpny_inevnoyr > 0:
        vs ybpny inevnoyr%20: 
            ahzoref.erzbir(ybpny_inevnoyr) 
        ybpny inevnoyr-1 
    erghea ahzoref

zl frg  = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1)}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny inevnoyr = 10 
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr 
    tybony inevnoyr += 10

sbe v va enatr(5):
    cevag(v) 
    v += 1 
vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10: 
    cevag("Pbaqvgvba zrg!") 

vs 5 abg va z1_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!") 
cevag(tybony_inevnoyr)
cevag(zl_qvpg) 
cevag(zl_frg)
"""

decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
