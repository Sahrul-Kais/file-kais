def createTri(n):
    for i in range(0,n):
        for j in range(0,n):
            print(end=" ")
        n = n-1
        for k in range(0,i+1):
            print("* ", end="")
        print("")
createTri(10)