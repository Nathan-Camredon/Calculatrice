#---------------------------
#         Import 
#---------------------------
from modules.comp_op import sin, cos, tan, percent, rad

#Function
def parenthesis(H):
    while ")" in H:
        try:
            j = H.index(")")
            i = -1
            for k in range(j-1, -1, -1):
                if H[k] == "(":
                    i = k
                    break
            if i == -1:
                break
            E = H[i+1:j]
            res = prep_c(E)[0]
            H = H[:i] + [res] + H[j+1:]
        except ValueError:
            break
    return H

def prep_c(A):
    i = 0
    while i < (len(A)):
        if A[i] == "sin":
            try:
                C = sin(rad(A[i+1]))
                A = A[:i] + [C] + A[i+2:]
            except:
                print("Erreur de valeur de sinus")
                return False
        elif A[i] == "cos":
            try:
                C = cos(rad(A[i+1]))
                A = A[:i] + [C] + A[i+2:]
            except:
                print("Erreur de valeur de cosinus")
                return False
        elif A[i] == "tan":
            try:
                C = tan(A[i+1])
                A = A[:i] + [C] + A[i+2:]
            except:
                print("valeur de tangeante invalide")
                return False
        elif A[i] == "rad":
            try:
                C = rad(A[i+1])
                A[:i] + [C] + A[i+2:]
            except:
                print("Erreur de valeur de radiant")
                return False
        else:
            i += 1
    i = 0
    while i < (len(A)):
        if A[i] == "/" or A[i] == "*": 
            try:
                C = 0
                if A[i] == "/":
                    C = A[i-1] / A[i+1]
                if A[i] == "*":
                    C = A[i-1] * A[i+1]
                A = A[:i-1] + [C] + A[i+2:]
                i -= 1 
            except:
                print("Division par 0 impossible")
                return False
        else:
            i += 1
    i = 0 
    while i < (len(A)):
        if A[i] == "+" or A[i] == "-":
            C = 0
            if A[i] == "+":
                C = A[i-1] + A[i+1]
            if A[i] == "-":
                C = A[i-1] - A[i+1]
            A = A[:i-1] + [C] + A[i+2:]
            i -= 1
        else:
            i += 1 
    i = 0 
    while i < (len(A)):
        if A[i] == "percent":
            C = percent(A[i-1], A[i+1])
            A = A[:i-1] + [C] + A[i+2:]
        else:
            i += 1  
    return A

def result(L):
    L = parenthesis(L)
    L = prep_c(L)
    
    if L:
        print("Résultat final :", L[0])
        return L
