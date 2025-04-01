time1 = input("Informe o nome do time: ")
gol1 = int(input("informe a quantidade de gols: "))
time2 = input("Informe o nome do segundo time: ")
gol2 = int(input("Informe a quantidade de gols: "))
if gol1 > gol2:
    print (f"O {time1} foi o vencedor por {gol1 - gol2} gol(s) de diferença!!")
elif gol1 == gol2:
    print (f"Empate!!")
else:
    print (f"O {time2} foi o vencedor por {gol2 - gol1} gol(s) de diferença!!!!")