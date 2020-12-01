# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 
import re
palavra = input("Digite uma palavra:").upper()
palavra_vogais =  re.findall(r'A|E|I|O|U', palavra)
palavra_espacos =  re.findall(r' ', palavra)

print(f'As vogais aparecem: {len(palavra_vogais)}')
print(f'Osespaços aparencem: {len(palavra_espacos)}')



