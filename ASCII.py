print(chr(65))     # prints ASCII  character
print(ord("A"))    # prints ASCII decimal number
print()
encrypt = input("Enter a word to encrypt: ")
encrypted = ""
for letter in encrypt:
    i = ord(letter)+5
    newletter = chr(i)
    encrypted += newletter

print(encrypted)

decrypt = input("Enter a word to decrypt: ")
decrypted = ""
for letter in decrypt:
    i = ord(letter)-5
    newletter = chr(i)
    decrypted += newletter

print(decrypted)
