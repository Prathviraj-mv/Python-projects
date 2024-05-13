MORSE_CODE_DICT = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',

    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',

    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',

    '9': '----.', '0': '-----', ' ': '   '
}
word = input("ENTER TEXT=")
list = []
def morse_convertor():
    for letter in word:
        list.append(letter.upper())
    print(list)
    morse_code = ""
    for letters in list:
        morse_code += MORSE_CODE_DICT[letters] + "  "
    return morse_code.strip()

print(f"MORSE_CODE={morse_convertor()}")

