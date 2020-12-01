# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

def user_inputs():
    """ 
    Função que recebe o valor do salário por hora,
    a quantidade de horas trabalhadas e calcula o salário bruto.
    
    args:
        salario_por_hora: Valor do salário por hora.
        horas_trabalhadas: Quantidade de horas trabalhadas no mês.
        salario_bruto: Valor do salário bruto.
    
    return: 
        O valor do salário bruto.
    """
    
    
    salario_por_hora = float(input("Quanto você ganha por hora? "))
    horas_trabalhadas = int(input("Quantas horas você trabalhou no mês? "))
    salario_bruto = salario_por_hora * horas_trabalhadas
    
    return salario_bruto

def calcula_impostos(salario_bruto):
    imposto_de_renda = salario_bruto * 11/100
    inss = salario_bruto * 8/100
    sindicato = salario_bruto * 5/100
    salario_liquido = sindicato-(inss-(salario_bruto - imposto_de_renda))
    return salario_bruto, imposto_de_renda, inss, sindicato, salario_liquido

def imprime_salario(imposto_de_renda,salario_bruto, inss,sindicato,salario_liquido):
    print(f"Salario Bruto: R${salario_bruto}")
    print(f'IR 11%: R${imposto_de_renda}')
    print(f'INSS 8%: R${inss}')
    print(f'Sindicato 5%: R${sindicato}')
    print(f'Salário líquido: R${salario_liquido}')

bruto = user_inputs()
a, b, c, d, e = calcula_impostos(bruto)
imprime_salario(a, b, c, d, e )
