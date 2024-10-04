'''
titulo: aumento salarial
autor: juan favtta
data: 26/09/2024

'''

#entrada de dados
salario = float(input ('digite o salario'))
#processamento de dados 
if salario < 1000:
    salario_reajuste = salario * 1.25
if salario >= 1000 and salario < 2000:
    reajuste = salario * 0.15
    salario_reajuste = salario + reajuste
if salario >= 2000:
    salario_reajuste = salario * 1.1
#saida de dados
print('seu novo salario:', salario_reajuste)