# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
a = int(input("Digite um lado: "))
b = int(input("Digite um lado: "))
c = int(input("Digite um lado: "))
if a >= (b + c):
    print("Não forma triâgulo")
else:
    if a != b != c :
        print("Triâgulo Escalenno")
    if c == a == b:
        #n sabia q dava pra comparar assism
        print("Triâgulo equilátero")
    elif a == b or b == c or a == c:
        print("Triâgulo isósceles")
