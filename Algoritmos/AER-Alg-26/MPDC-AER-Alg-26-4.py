def codigo_morse(texto):
    codigos = {'A': '.-',   'B': '-...',    'C': '-.-.',    'D': '-..',
        'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
        'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
        'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
        'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
        'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
        '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
        '8': '---..',    '9': '----.',   ' ': '\n'
        }
        
    morse = ' '
    for char in texto:
        morse = codigos[char]
        if char != " ":
            print("{} = {}".format(char, morse))
        else:
            print(morse)

def main():
    texto = input('Digite aqui o texto: ').upper()  
    codigo_morse(texto)

if __name__ == "__main__":
    main()