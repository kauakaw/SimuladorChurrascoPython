# -*- coding: utf-8 -*-
"""Churrasco

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n_IMqGHQuAS47i_IgcxyvKf9mXbkXbD7
"""

import time

qtdCarneHom = 0.5 #400g
qtdFrangoHom = 0.2 #200g
qtdCervejaHom = 4 #homem bebe 4 latas de cerveja
qtdRefriHom = 0.25 #500ml de Refri
qtdCarvao = 1 #1 pacote para cada 10 pessoas

qtdCarneMul = 0.3 #400g
qtdFrangoMul = 0.1 #200g
qtdCervejaMul = 2 #homem bebe 4 latas de cerveja
qtdRefriMul = 0.25 #500ml de Refri

qtdCarneCria = 0.2 #400g
qtdFrangoCria = 0.1 #200g
qtdCervejaCria = 0 #homem bebe 4 latas de cerveja
qtdRefriCria = 0.125 #500ml de Refri

precoCarne = 50.0 #kg contra filé
precoFrango = 23.0 #kg tulipa
precoCerveja = 3.99 #lata Heineken 269ml
precoRefri = 8.0 #garrafa 2l
precoCarvao = 25.0 #pacote 4g

#Capturar informações

print("Bem-vindos a calculadora de churrasco")
print()
homens = float(input("Quantos homens vão no churrasco?: "))
mulheres = float(input("Quantas mulheres vão no churrasco?: "))
criancas = float(input("Quantas crianças vão no churrasco?: "))

#Calculo de peso

carneHom = homens * qtdCarneHom
carneMul = mulheres * qtdCarneMul
carneCria = criancas * qtdCervejaCria

FrangoHom = homens * qtdFrangoHom
FrangoMul = mulheres * qtdFrangoMul
FrangoCria = criancas * qtdFrangoCria

cervejaHom = homens * qtdCervejaHom
cervejaMul = mulheres * qtdCervejaMul

refriHom = homens * qtdRefriHom
refriMul = mulheres * qtdRefriMul
refriCria = criancas * qtdRefriCria

carvaoPacotes = (homens + mulheres + criancas) / 10

#Criar os calculos de gastos

valorCarneHom  = carneHom * precoCarne
valorCarneMul = carneMul * precoCarne
valorCarneCria = carneCria * precoCarne

valorfrangoHom  = FrangoHom * precoFrango
valorfrangoMul = FrangoMul * precoFrango
valorfrangoCria = FrangoCria * precoFrango

valorCervejaHom = cervejaHom * precoCerveja
valorCervejaMul = cervejaMul * precoCerveja


valorRefriHom  = refriHom * precoRefri
valorRefriMul = refriMul * precoRefri
valorRefriCria = refriCria * precoRefri

valorCarvao = precoCarvao * carvaoPacotes

total = valorCarneCria + valorCarneHom + valorCarneMul + valorfrangoCria + valorfrangoHom + valorfrangoMul + valorCervejaHom + valorCervejaMul + valorRefriCria + valorRefriHom + valorRefriMul

#apresentar os dados

print(f'Total de pessoas Homens: {homens}, Mulheres: {mulheres}, Crianças: {criancas} \n')

print(f'Lista de compras: {carneCria + carneHom + carneMul } kg de carne.')
print(f'                  {FrangoCria + FrangoHom + FrangoMul } kg de frango.')
print(f'                  {refriCria + refriHom + refriMul } garrafas de refrigerante.')
print(f'                  {cervejaHom + cervejaMul} latas de cerja.')
print(f'                  {carvaoPacotes} pacotes de carvão. \n')

print(f'Valor total da compra: R${round(total, 2)}')
print(f'Valor por convidado: {round(total / (homens + mulheres + criancas), 2)}')

"""print('Calculando...')
time.sleep(1)
print('Calculando...')
time.sleep(1)
print('Calculando... \n')
time.sleep(1)
"""