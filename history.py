def history(save):

    with open("history.txt", "a") as file:
         file.write(str(save))
         file.write(" ")




    #file = open("history.txt","a")
    #file.write(str(save))
    #file.close
    return  save
