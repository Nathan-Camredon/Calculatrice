
a = (input("Entrez une operation :  "))
tokens = a.split()

def analyse_chiffre(token):
    """Permet de vérifier si c'est un float ou un int ou string"""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

tokens_analyse = []
for token in tokens:
    tokens_analyse.append(analyse_chiffre(token))
print(tokens_analyse)

