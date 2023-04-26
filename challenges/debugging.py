#EXERCISE1
def say_hello(name):
    return "hello {name}"

#SOLUTION
def say_hello(name):
    return f"hello {name}"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"

#EXERCISE 2
# def encode(text, key):
#     cipher = make_cipher(key)
#     ciphertext_chars = []
#     for i in text:
#         ciphered_char = chr(65 + cipher.index(i))
#         ciphertext_chars.append(ciphered_char)
#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)
#     plaintext_chars = []
#     for i in encrypted:
#         plain_char = cipher[65 - ord(i)]
#         plaintext_chars.append(plain_char)
#     return "".join(plaintext_chars)


# def make_cipher(key):
#     alphabet = [chr(i + 98) for i in range(1, 26)]
#     cipher_with_duplicates = list(key) + alphabet
#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])
#     return cipher

# # When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)
# EXERCISE 2 solution:

def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
    return "".join(ciphertext_chars)

def decode(encrypted, key):
    cipher = make_cipher(key)
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)
    return "".join(plaintext_chars)

def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    return cipher

#['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

dict.get()

#Debugging challenge

def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), reverse=True, key=lambda item: item[1])[0][0]
    #changing from [1] to [0] allowed it to return the key rather than the value. Remember .items() turns dict into list and tuples, so accessing via indices works again
    return letter
print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")