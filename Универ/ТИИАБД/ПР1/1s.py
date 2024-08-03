def encode_morse(text):
    morze = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..'
    }
    words = text.split()
    encoded_words = []
    for word in words:
        encoded_word = ' '.join([morze.get(letter.lower()) for letter in word])
        encoded_words.append(encoded_word)
    return encoded_words

text = input("Введите текст на английском языке: ")
result = encode_morse(text)
for word in result:
    print(word)