import keyboard

print("\n \n~~ Pour afficher les opération possibles veuillez taper sur la touche ! de votre clavier ~~\n \n ")

def press_key():
    print("\n\nVous pouvez utiliser : PI | % | carre | rad | sin | cos | tan")
keyboard.add_hotkey("!", press_key)


def scan_number(number):
    """Allows you to check if it's a float, an int, or a string"""
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            return number

def number_inc():
    """Input for number and check if operator is first """
    inc = (input("Entrez une operation :  "))
    inc = add_space(inc)
    if not inc or inc.isspace():
        return []

    list = inc.split()

    list_analyse = []
    for number in list:
        list_analyse.append(scan_number(number))
    
    if list_analyse and (list_analyse[0] == "+" or list_analyse[0] == "-"):
        list_analyse.insert(0, 0)
    return list_analyse

def add_space(a):
    """Add space between number and operator"""

    operator = {"+", "-", "*", "/", "%", "(", ")", }
    comp_operator = {"sin", "cos", "tan", "rad", "carre", "sqrt", "PI"}

    for i in comp_operator:
        a = a.replace(i, f" {i} ")
    
    for i in operator:
        a = a.replace(i, f" {i} ")
    while "  " in a:
        a = a.replace("  ", " ")

    return a.strip()


def erase():
    try:
        1 == 0
    except KeyboardInterrupt:
        list_analyse = []
