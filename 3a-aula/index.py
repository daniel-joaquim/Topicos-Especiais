# -- coding: utf-8 --

# 1. Informe dois valores numéricos e determine se é maior, menor ou igual. Quando for maior,
# apresente a mensagem 'Valor X é maior que valor Y', quando for menor apresente a
# mensagem 'Valor X é menor que valor Y', quando for igual apresente a mensagem 'Os
# valores de X e Y são iguais'. Utilize o método input para informar os valores e o método
# print para mostrá-los.


valor_x = int(input("Informe o valor X: "))
valor_y = int(input("Informe o valor Y: "))

if valor_x > valor_y:
    print("Valor X ({}) é maior que valor Y ({})".format(valor_x, valor_y))
elif valor_x < valor_y:
    print("Valor X ({}) é menor que valor Y ({})".format(valor_x, valor_y))
else:
    print("Os valores de X ({}) e Y ({}) são iguais".format(valor_x, valor_y))

# 2. Informe dois valores de texto e determine se são iguais ou diferentes. Quando for igual
# apresente a mensagem 'Os valores informados são iguais', quando for diferente
# apresente as mensagens 'Valor X é diferente do valor Y'. Utilize o método input para
# informar os valores e o método print para mostrá-los.

texto_x = input("Informe o valor de texto X: ")
texto_y = input("Informe o valor de texto Y: ")

if texto_x == texto_y:
    print("Os valores informados são iguais")
else:
    print("Valor X ('{}') é diferente do valor Y ('{}')".format(texto_x, texto_y))

# 3. Faça um loop utilizando for e imprima os valores de 1 até 10 em sequência.

for i in range(1, 11):
    print(i)

# 4. Faça um loop utilizando while e imprima os valores de 1 até 10 em sequência.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# 5. Dado a seguinte lista de dados {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro',
# 'd': 'quarto', 'e': 'quinto'} , imprima as seguintes informações de cada dado:
# índice na lista, chave e valor.

dados = {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro', 'd': 'quarto', 'e': 'quinto'}

for indice, (chave, valor) in enumerate(dados.items()):
    print("Índice: {}, Chave: {}, Valor: {}".format(indice, chave, valor))

# 6. Dado a seguinte lista de dados [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3] , imprima
# os seguinte valores 1, 2, 5 e 6 . Devem ser impressos somente esses dados e
# exatamente nessa ordem. Obs: utilize recursos do list e da estrutura de loop para resolver
# da melhor maneira.

lista_dados = [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3]
valores_para_imprimir = [1, 2, 5, 6]

for valor in lista_dados:
    if valor in valores_para_imprimir:
        print(valor)