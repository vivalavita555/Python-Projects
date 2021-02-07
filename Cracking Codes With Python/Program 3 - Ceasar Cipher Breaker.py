SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
message = input("Enter the encrypted message: \n>")

#Loop through every possible key:
for key in range(len(SYMBOLS)):
    translated = ''

    #Loop through each symbol in message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #Handle the wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            #Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]
        
        else:
            #Append the symbol without encrypting/decrypting
            translated = translated + '#'
        
    #Display every possible decryption:
    print('Key #%s: %s' %(key, translated))
print('The # symbol means the symbol wasn\'t found!')