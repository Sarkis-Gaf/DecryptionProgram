# This defines all of the decrypted letters I manually parsed through the text and found.
full_substitutions = {
    'v': 't', 'i': 'h', 'k': 'e', 'z': 'a', 'b': 'n', 'm': 'd', 'q': 'i', 'u': 's',
    'l': 'o', 's': 'u', 'j': 'c', 'h': 'y', 'a': 'r', 'g': 'w', 'f': 'm', 'x': 'b',
    'c': 'g', 'r': 'f', 't': 'l', 'e': 'p', 'y': 'v', 'p': 'k', 'w': 'z', 'n': 'j',
    'o': 'x', 'd': 'q'
}

# This function will substitute all of the letters in the text using the mapping
def substitute_letters(text, mapping):
    return ''.join(mapping.get(char, char) for char in text)

# Read the original ciphertext from the file
with open("ciphertext.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read()

# Perform the full substitution
fully_decrypted_text = substitute_letters(ciphertext, full_substitutions)

# Write the fully decrypted text to a new file
with open("full_decryption.txt", "w", encoding="utf-8") as file:
    file.write(fully_decrypted_text)

print("Full decryption complete! Check 'full_decryption.txt'.")