def valid_parentheses(string):
    if string.startswith(')') or string.endswith('('):
        return False
    elif string.count('(') != string.count(')'):
        return False
    elif string.find(')') < string.find('('):
        return False
    else:
        return True
