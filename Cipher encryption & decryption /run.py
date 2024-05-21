alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
while True:
    text = input('ENTER THE TEXT:')
    shift = input('ENTER THE SHIFT NUMBER')
    choice = input("1 = ENCRYPT OR 2 = DECRYPT ")

    choice = int(choice)
    text = text.lower()


    def encrypt(input_text, input_shift):
        cipher = ""
        for letter in input_text:

            letter_position = alphabet.index(letter)
            new_letter_position = letter_position + int(input_shift)
            if new_letter_position > 26:
                new_letter_position -= 26
            new_letter = alphabet[new_letter_position]
            cipher += new_letter

        return f"ENCRYPTED TEXT = {cipher} ."


    def decrypt(input_text, input_shift):
        de_cipher = ""
        for letter in input_text:

            letter_position = alphabet.index(letter)
            new_letter_position = letter_position - int(input_shift)
            if new_letter_position < 0:
                new_letter_position += 26
            new_letter = alphabet[new_letter_position]
            de_cipher += new_letter
        return f"DECRYPTED TEXT = {de_cipher} ."



    if choice == 1:
        print(encrypt(input_text=text, input_shift=shift))
    if choice == 2:
        print(decrypt(input_text=text, input_shift=shift))
