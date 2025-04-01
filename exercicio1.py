n = input("Informe seu nome: ")
i = int(input('informe sua idade: '))
s = float(input("informe seu salário: "))
p = float(input("Informe o percentual de aumento em porcentagem: "))
sa = s + s * (p/100)
print (f"Seu nome é {n}, você tem {i} anos e seu salário é \033[1;31;42mR${s:.2f}\033[m reais")
print (f"Com o aumento de {p}%, o salário será {sa}")

# pedir percentual de aumento, calcular o percentual e pedir o valor com o p