# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# tamanho em m² da área a ser pintada. 
metros_quadrados = float(input("Qual o tamanho da áre a ser pintada? "))

# entradas
litros_lata = 18 ; custo_lata = 80
metro_litro = 6
litros_galoes = 3.6 ; custo_galao = 25

# processamento
litros_por_metros = metros_quadrados / metro_litro
litros_sobra_lata =  litros_por_metros - litros_lata 
litros_sobra_galao =  litros_por_metros - litros_galoes 

def mensagem_latas():
    print(f"""Com latas
Para pintar uma area de {metros_quadrados}m².
gastará um total de {litros_por_metros}L. E tera que pagar R${custo_lata} e sobrará {abs(litros_sobra_lata)} litros""")

def mensagem_galao():
    print(f"""Com Galão
Para pintar uma area de {metros_quadrados}m².
gastará um total de {litros_por_metros}L. E tera que pagar R${custo_galao} e sobrará {abs(litros_sobra_galao)} litros""")


if litros_por_metros > litros_lata:
    while litros_por_metros > litros_lata:
        litros_lata = litros_lata + litros_lata
        custo_lata = custo_lata + custo_lata
        litros_sobra_lata =  litros_por_metros-litros_lata 
        
        if litros_por_metros <= litros_lata:
            mensagem_latas()
            break
        else:
            continue
elif litros_por_metros <= litros_lata:
    mensagem_latas()       

##########################################
if litros_por_metros > litros_galoes:
    while litros_por_metros > litros_galoes:
        litros_galoes = litros_galoes + litros_galoes
        custo_galao = custo_galao + custo_galao
        litros_sobra_galao =  litros_por_metros - litros_galoes 
        
        if litros_por_metros <= litros_galoes:
            mensagem_galao()
            break
        else:
            continue
elif litros_por_metros <= litros_galoes:
    mensagem_galao()

###########################################

if litros_sobra_lata > litros_galoes:
    pass
#faltou a misturo dos dois tipos de tinta