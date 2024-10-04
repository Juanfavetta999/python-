'''
titulo: mes por extenso
autor: juan favetta
data: 26/09/2024
descrição: faça um programa que receba o mes em número e apresente por extremo.

'''

#entrad de dados
mes = int(input('inserir o número mes:'))
#processamento de dados
if mes == 1:
    mes_extenso = 'janeiro'
elif mes == 2:
    mes_extenso = 'fevereiro'
elif mes == 3:
    mes_extenso = 'março'
elif mes == 4: 
    mes_extenso = 'abril'
elif mes == 5: 
    mes_extenso = 'maio'
elif mes == 6:
    mes_extenso = 'junho'
elif mes == 7:
    mes_extenso = 'julho'
elif mes == 8:
    mes_extenso = 'agosto'
elif mes == 9:
    mes_extenso = 'setembro'
elif mes == 10:
    mes_extenso = 'outubro'
elif mes == 11:
    mes_extenso = 'novenbro'
elif mes == 12:
    mes_extenso = 'dezembro'
else:
    mes_extenso = 'mes não existe'
#saida de 
print(mes_extenso)

titulo: categoria pela idade
autor: juan favetta
data: 01/10/2024
descrição: 
 
idade = input('digite a idade')
if idade <=12 : 'criança'
elif idade >=13 and idade <=17: 'adolesente'
elif idade >=18 and idade <=59: 'adulto'
elif idade >=60 and idade <= : 'especialista'  