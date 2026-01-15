import keyboard

operator = "+*/-"

print("\n \n~~ Pour afficher les opération possibles veuillez taper sur la touche A de votre clavier ~~\n \n ")

def press_key():
    print("\n\nVous pouvez utiliser : PI | % | carre | rad | sin | cos | tan")
keyboard.add_hotkey("a", press_key)


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
    """Input for number and check if operator is first """
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
    """Add space between number and operator"""
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
