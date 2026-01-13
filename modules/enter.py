
inc = (input("Entrez une operation :  "))
tokens = inc.split()

def scan_number(token):
    """Allows you to check if it's a float, an int, or a string"""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

tokens_analyse = []
for token in tokens:
    tokens_analyse.append(scan_number(token))
print(tokens_analyse)
