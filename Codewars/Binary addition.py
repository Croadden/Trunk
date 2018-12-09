# Take 2 numbers and turn them into binary

def add_binary(a, b):
    result = ''
    sum = a + b
    while sum >= 1:
        if sum == 1:
            result += '1'
            break
        elif sum % 2 == 0:
            result += '0'
            sum = sum / 2
        else:
            result += '1'
            sum = sum / 2
    return result[::-1]
