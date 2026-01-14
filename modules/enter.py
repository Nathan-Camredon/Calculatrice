operator = "+-*/()"

def scan_number(token):
    """Allows you to check if it's a float, an int, or a string"""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

def number_inc():
    inc = (input("Entrez une operation :  "))
    inc = add_space(inc)
    if not inc or inc.isspace():
        return []

    tokens = inc.split()

    tokens_analyse = []
    for token in tokens:
        tokens_analyse.append(scan_number(token))
    
    if tokens_analyse and (tokens_analyse[0] == "+" or tokens_analyse[0] == "-"):
        tokens_analyse.insert(0, 0)
    return tokens_analyse

def add_space(a):
    result = ""
    for c in a:
        if c in operator:
            result += " " + c + " "
        else:
            result += c
    return result

def erase():
    try:
        1 == 0
    except KeyboardInterrupt:
        tokens_analyse = []
