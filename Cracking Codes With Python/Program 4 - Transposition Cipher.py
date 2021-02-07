import pyperclip

def main():
    message = input("Please enter your message: \n>")
    key = int(input("Please enter your key: \n>"))

    ciphertext = encryptMessage(key, message)

    # Print the encrypted string in ciphertext to the screen, with
    # a | after it in case there are spaces at the end of the message:
    print(ciphertext + '|')

    # Copy the encrypted message to the clipboard
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key 

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key 

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)

# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main function
if __name__ == '__main__':
    main()