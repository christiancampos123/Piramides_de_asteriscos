altura = 10
distancia = altura
i=0
prin=0
for z in range(altura):
    while prin < distancia:
        print(end=" ")
        prin = prin+1
    print("*", end="")
    for w in range(i):
        print(" *",end="")

    i = i+1
    prin = i
    print()