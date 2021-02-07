message = input("Type the message you want encrypted/decrypted: ")
translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)