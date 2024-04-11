# -*- coding: utf-8 -*-
"""Atividade Python 28/02/24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EtOM_ixn0THEKV0WKWxpedXert6_3pqp

# EXERCÍCIOS 28/02/24

1 - Faça um Programa que mostre a mensagem "Olá, mundo!" na tela.
"""

print('Olá, mundo! :)')

"""2 - Faça um Programa que peça um número e então mostre a mensagem ."""

a=input('Digite um número:')
print(a)

"""3 - Faça um Programa que peça dois números e imprima a soma."""

h=int(input('Digite um número inteiro:'))
t=int(input('Digite um número inteiro:'))
print(f'A soma dos números é {h+t}')

"""4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.**

> Bloco com recuo


"""

#1º modo de fazer:
d=float(input('Digite a primeira nota: '))
e=float(input('Digite a segunda nota: '))
f=float(input('Digite a terceira nota: '))
g=float(input('Digite a quarta nota: '))
x = (d+e+f+g)/4
print(f'A média das quatro notas é: {x}')

#2º modo de fazer:
soma = 0

for i in range(0,4):
  notas=float(input(f'Digite uma nota {i+1}: '))
  soma += notas
med=soma/4

print('A média das notas é {med:.2f}')

"""5 - Faça um Programa que converta metros para centímetros.

"""

m=float(input('Digite uma medida de comprimento em metros:'))
cm=float(m*10**2)
print(f'Em centímetros esse valor é: {cm}')

"""6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

r=(float(input('Determine um raio de um círculo:')))
a=2*r*3.14
print(f'A área do círculo é: {a:.2f}')

"""7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

"""

l=(float(input('Insira a medida de um lado de quadrado:')))
a=l**2
print(f'O dobro da área desse quadrado é: {2*a}')

"""8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""

s=(float(input('Quanto você recebe por hora de trabalho? ')))
h=(float(input('Quantas horas você trabalha por dia? ')))
print(f'O seu salário é: {s*h}')

"""9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

"""

F=float(input('Insira uma temperatura em graus Fahrenheit, please: '))
print(f'A temperarua inserida equivale, em graus Celsius, a: {5 * ((F-32) / 9)}')

"""10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

C=float(input('Insira uma temperatura em graus Celsius, please: '))
print(f'A temperarua inserida equivale, em graus Fahrenheit, a: {(C*1.8)+32}')

"""11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo;
- a soma do triplo do primeiro com o terceiro;
- o terceiro elevado ao cubo.
"""

a=int(input('Insira um número inteiro: '))
b=int(input('Insira um segundo número inteiro: '))
c=float(input('Insira um número real: '))

print(f'O dobro do primeiro número com metade do segundo é: {(2*a) + (b/2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(3*a)+c}')
print(f'O terceiro elevado ao cubo é: {c**3}')

"""12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (**50 quilos**) deve pagar uma multa de **R$ 4,00 por quilo excedente**. **João precisa que você faça um programa que leia a variável  (peso de peixes) e calcule o excesso. Gravar na variável  a quantidade de quilos além do limite e na variável  o valor da multa que João deverá pagar.** Imprima os dados do programa com as mensagens adequadas.

"""

p=float(input('Digite o peso do peixe em quilos: '))
if p>50:
  exced=p-50
  multa=exced*4.00
  print(f'O peixe excede o regulamento em ', exced, ' kg. Portantó a multa é de ', multa, ' reais.')
else:
  print(f'O peso do peixe está dentro dos pradões do regulamento. Portanto, não há taxa.')

"""13 - Faça um Programa que pergunte **quanto você ganha por hora e o número de horas trabalhadas no mês**. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são **descontados 11% para o Imposto de Renda**, **8% para o INSS** e **5% para o sindicato**, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.


Obs.: Salário Bruto - Descontos = Salário Líquido.

"""

h=float(input('Quanto você ganha por hora de serviço? '))
m=float(input('Quantas horas você trabalha por mês? '))
salbruto=h*m

imprenda=salbruto*0.11
inss=salbruto*0.08
sindicato=salbruto*0.05
salliquido = salbruto - imprenda - inss - sindicato

print(f'O sálario líquido é: ', salliquido)

"""14 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de **1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00**. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

tam=float(input('Determine o tamenho, em metros, da área a ser pintada: '))
#Cada lata pinta 54m, já que cada 1l cobre 3m.
latas=tam/54
preco=latas*80
print('A quantidade de latas necessárias é', latas, '. E o preço total é ', preco, '.')

"""### 15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

#2º resolução
tam=float(input('Determine o tamanho, em metros, da área a ser pintada: '))

#só latas
quantlatas=int(tam/54)
precol=quantlatas*80
print('No caso das latas de 18l, arredondando, deve-se comprar', quantlatas, '. O custo será de', precol, '.')

#só galões
quantgalao=int(tam/21.6)
precog=quantgalao*25
print('No caso dos galões de 3.6l, arredondando, deve-se comprar', quantgalao, '. O custo será de', precog, '.')

#latas e galões
latasint=int(tam/18)
galrest=int(tam % 18)/3.6
precomisto=int(latasint*80) + int(galrest*25)
print(f'No caso de latas e galões, deve-se comprar',latasint,'latas e',galrest,'galões. O custo misto será de',precomisto,'.')

tam=float(input('Determine o tamanho, em metros, da área a ser pintada: '))

#só latas
latas=int(tam/18)
precolat=latas*80.

#só galões
galao=int(tam/3.6)
precogal=galao*25

#latas e galões
latasint=int(tam/18)
galrest=int(tam % 18)/3.6
precomisto=int(latasint*80) + int(galrest*25)

print('No caso das latas de 18l, deve-se comprar ', latas, '. O custo seá de ', precolat, '.')
print('No caso dos galões de 3.6l, deve-se comprar ', galao, '. O custo seá de ', precogal, '.')
print('No caso de a pintura ser feita com latas e galões, deve-se comprar ', latasint, ' latas e ', galrest, ' galões. E o valor total será ', precomisto, ' reais.')
#A quantidade de galões continou dando números decimais pequenos. Ele pediu mínimo de desperdícios, mas não dá pra comprar 0,5 galão.
#Então de toda forma o valo ficou arrendoda para 893, pois pedi pra contar o valor de 1 galão e latas inteiras de tinta(também não se compra só uma parte da lata de tinta).
#Fiz o que pude, Helen.

"""16 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

MB=float(input('Insira o tamanho de um arquivo para dowload: '))
MBPS=float(input('Insira a velocidade de um link de Internet: '))


convsMB=MB*8 #conversão de tamanho do arquivo MP para MBPS
tempsegundos=convsMB/MBPS
tempminutos=tempsegundos/60

print(f"O tempo aproximado de download do arquivo é de {tempminutos:.2f} minutos.")

# Passo a passo:
# 1) Converter o MB para MBPS(multiplicando por 8).
# 2) Dividir um pelo outro para ter o tempo em segundo.
# 3) Dividir por 60, para transferir de segundos para minutos.