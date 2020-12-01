# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 
from random import randrange

lista_de_resultados = []
for i in range(0, 101):
    lacar_dado = randrange(1,7)
    lista_de_resultados.append(lacar_dado)

for i in range(1, 7):
        quantidade = lista_de_resultados.count(i)
        print(f'{i}: {quantidade}')

