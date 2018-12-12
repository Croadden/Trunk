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


def binary_search(list, item):
    if len(list) == 1 and item in list:
        return item
    sub_list = list[1:]


my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 1)
print binary_search(my_list, -1)
