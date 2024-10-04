'''
Algorismo "conversão de unidades"
Descrição : faça as conerções a seguir e mostre os resultado.
- polegadas;
- jardas;
- milhas; 
Sabe -se que: 1 pé = 12

polegadas; 
1 jarda = 3 pé;
1 milha = 1.760

jarda;
autor (a) : juan favetta
data atual : 24/09/2024
'''
#entrada de dados
pes = int(input('inserir o valor em pés:'))
#processamentos de dados
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760
#saida de dados
print('polegadas:', polegadas)
print('jkardas:', polegadas)
print('milhas:', milhas)