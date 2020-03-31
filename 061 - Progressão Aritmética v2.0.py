#   Exercício Python 061 - Progressão Aritmética v2.0
#   Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#   mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 11:
    print('{} - ' .format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
