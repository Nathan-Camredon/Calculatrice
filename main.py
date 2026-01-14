#---------------------------
#         Import 
#---------------------------
from modules.enter import number_inc
from modules.result import result
#---------------------------
#         Fonction
#---------------------------
def main():
    try:
        while True:
            L = number_inc()
            result(L)
    except KeyboardInterrupt:
        print("\nAu revoir !")
main()