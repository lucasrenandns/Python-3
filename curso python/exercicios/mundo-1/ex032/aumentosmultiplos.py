salario = float(input("Qual é o salário do funcionário? R$ "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("O funcionário que ganhava R${:.2f} passará a ganhar R${:.2f} agora".format(salario, novo))