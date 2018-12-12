def make_password(phrase):
    letters = phrase.strip().split()
    words = [words[:1] for words in letters]
    maker = {"I": '1',
             'i': '1',
             'o': '0',
             'O': '0',
             "s": '5',
             "S": '5'}
    for letters in words:
        if letters in maker:
            words.insert(words.index(letters), letters.replace(letters, str(maker.get(letters))))
            words.remove(letters)
    string = ''
    return string.join(words)


print make_password('Keep Calm and Carry On')
