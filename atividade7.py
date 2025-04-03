c = input("Qual o tipo de combustível? Escreva G para gasolina e E para etanol: ").strip()
v = float(input("Informe a quantidade de litros: "))
if c[0] == 'e' or 'E':
    r = v * 4.9
    print (f"O valor será R${r:.2f}")
elif c[0] == 'g' or 'G':
    r = v * 5.8
    print (f"O valor será R${r:.2f}")
else:
    r = v * 0
    print(f"Resposta inválida. Valor R${r:.2f}")

