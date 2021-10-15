""" 
Marcela Fuentes, A01748161
Katia Bellido, A01023638
Carla Pérez Gavilán, A01023033
16/03/2021

Vigenere: uses a keyword were each character determines the alphabet shift 
"""

def cipher(alpahbet, string, keyword):
    key = generate(string, keyword)
    result = []
    for i in range(len(string)):
        string_ix = alphabet.index(string[i])
        key_shift = len(alphabet) -alphabet.index(key[i])
        final_ix = (string_ix + key_shift) % len(alphabet) 
        result.append(alphabet[final_ix])
    return("".join(result))

def generate(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))

def decipher(alphabet, string, keyword):
    key = generate(string, keyword)
    result = []
    for i in range(len(string)):
        string_x = alphabet.index(string[i])
        key_shift = len(alphabet) - alphabet.index(key[i]) 
        final_ix = (string_x - key_shift ) % len(alphabet) 
        result.append(alphabet[final_ix])
    return("".join(result))

def max(array):
    max = 0
    index_max = 28
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            index_max = i
    return index_max

def get_key_statistics(alphabet, space, string):
    indexes_a = [0] * len(alphabet)
    indexes_b = [0] * len(alphabet)
    indexes_c = [0] * len(alphabet)
    indexes_d = [0] * len(alphabet)
    for i in range(len(string)):
        idx = alphabet.index(string[i])
        if (i%4 == 0 ):
            indexes_a[idx] += 1
        if (i%4 == 1 ):
            indexes_b[idx] += 1
        if (i%4 == 2 ):
            indexes_c[idx] += 1
        if (i%4 == 3 ):
            indexes_d[idx] += 1
    max_a = space - max(indexes_a)
    max_b = space - max(indexes_b)
    max_c = space - max(indexes_c)
    max_d = space - max(indexes_d)
    return alphabet[max_a]+alphabet[max_b]+alphabet[max_c]+alphabet[max_d]

if __name__ == "__main__":
    alphabet  = "abcdefghijklmnopqrstuvwxyz "
    path = './cipher2.txt'
    file = open(path,'r')
    string = file.read()
    keyword= get_key_statistics(alphabet, 26, string)
    print("\n  this is keyword: ", keyword)

   
    deciphered_text = decipher (alphabet, string, keyword)
    print("\n this deciphered text: " , deciphered_text)

    # Write on file
    file = open("decipher2.txt", "w")
    file.write(deciphered_text)

    # Second test
    encrypted = cipher(alphabet, "hola soy carla ", keyword)
    print("\n this is encrpyted: ", encrypted)

    decrypt = decipher(alphabet, encrypted, keyword)
    print("\n this is decrypted: ", decrypt)



    
