#---------------------------
#         Import 
#---------------------------
from modules.enter import number_inc
from modules.result import result
from history import history
#---------------------------
#         Fonction
#---------------------------
def main():
    try:
        while True:
            L = number_inc()
            res = result(L)
            if res:
                history(res[0])
    except KeyboardInterrupt:
        print("\nAu revoir !")
main()