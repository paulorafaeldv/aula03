c = input("Qual o tipo de combustível? Escreva G para gasolina e E para etanol: ").strip().lower()
v = float(input("Informe a quantidade de litros: "))
if c == 'e':
    r = v * 4.9
    print (f"O valor será R${r:.2f}")
elif c == 'g':
    r = v * 5.8
    print (f"O valor será R${r:.2f}")
else:
    r = v * 0
    print(f"Resposta inválida. Valor R${r:.2f}")

