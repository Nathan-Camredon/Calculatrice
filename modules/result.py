L = [12 , "+", 12, "/", 12, "*", 12, "-", 12, "*", "(", 12, "+", 12, ")"]

def parenthesis(H):
    i = 0
    while i < (len(H)):
        if H[i] == "(":
            j = i
            while j < (len(H)):
                j += 1 
                if j < len(H) and H[j] == ")":
                    E = H[i+1:j] 
                    res = prep_c(E)[0] 
                    
                    H = H[:i] + [res] + H[j+1:]
                    return H
        i += 1
    return H

def prep_c(A):
    i = 0
    while i < (len(A)):
        if A[i] == "/" or A[i] == "*": 
            C = 0
            if A[i] == "/":
                C = A[i-1] / A[i+1]
            if A[i] == "*":
                C = A[i-1] * A[i+1]
            A = A[:i-1] + [C] + A[i+2:]
            i -= 1 
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
    return A

def result(L):
    L = parenthesis(L) 
    L = prep_c(L)
    print("Résultat final :", L[0])


result(L)