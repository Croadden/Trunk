def expanded_form(num):
    text = ''
    array1 = []
    array = [i for i in str(num)]
    for i in array:
        if i != '0':
            array1.append(int(array[0]) * (10 ** (len(array) - 1)))
            array = array[1:]
        else:
            array = array[1:]
    for i in array1:
        text += '{} + '.format(i)
    return text[:-3]


print expanded_form(70304)  # Should return '70000 + 300 + 4'
