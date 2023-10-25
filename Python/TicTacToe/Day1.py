print("WELCOME TO TIC TAC TOE GAME:")
print("---------------------------")
rows =3
cols =3

def DisplayGameBoard():
    for x in range(rows):
        print("")
        if x>0:
            print(end= " ")
            print("-" * 9)
        for y in range(cols):
             print("", end=" |  ")
    
DisplayGameBoard()


#Create Matrix

def DisplayGameBoard(size):
    for x in range(size):
        if x>0:
            # print("")
            print(end="" )
            print(" " + ("- " * (size))*2)
        for y in range(size):
            print(" ", end =" | ")
        print("")
