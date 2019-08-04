def main():
    myMessage = raw_input('Message to encrypt: ')
    myKey = int(raw_input('Key to use: '))

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] = ciphertext[column] + message[currentIndex]

            currentIndex = currentIndex + key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
