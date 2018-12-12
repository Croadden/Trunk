def find_missing_letter(chars):
    compare_order = ord(chars[0])
    for letter in chars:
        if compare_order != ord(letter):
            return chr(compare_order)
        else:
            compare_order += 1
            pass


find_missing_letter(['a', 'b', 'c', 'd', 'f'])
