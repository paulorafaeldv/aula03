
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
m = (nota1 + nota2 + nota3)/3
if m >= 7:
    print (f"Sua média foi {m:.2f}. \033[32mParabens! Aprovado\033[m")
else:
    if m < 4:
        print(f"Sua média foi {m:.2f}. \033[31mReprovado\033[m")
    else:
        print(f"Sua média foi {m:.2f}. \033[33mEstá de recuperação\033[m")