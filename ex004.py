# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 
num = int(input("Verificar numeros primos ate: "))
lista =[]
for n in range(1,num + 1):
    if n % 2 == 1 :
        lista.append(n)


for n in lista:
    if n // 1 == 1 and n%3 == 0:
        lista.append(n)

#devia ter feito isso com tds os primos ate o 10 como eu fiz
print(lista)
