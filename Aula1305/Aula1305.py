'''
    Parte 1 - CRIE UMA CALCULADORA DE JUROS COMPOSTOS

capital = float(input('capital inicial para investimento: '))
tempo = int(input('Quanto tempo deseja manter o capital aplicado? (em meses): '))
juros = int(input('Qual a taxa de juros mensal: '))
taxa = float((juros / 100))
montante = "x"

def juros_compostos():
    global capital
    global tempo
    global taxa
    global montante
    montante = capital * (1 + taxa) ** tempo
juros_compostos()

print(f"Seu valor rentabilizado é de R${montante} reais.")
'''
'''
capital = 1000
tempo = 5
juros = 10
taxa = juros / 100
montante = "x"

def juros_compostos():
    global capital
    global tempo
    global taxa
    global montante
    montante = capital * (1 + taxa) ** tempo
juros_compostos()

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio')
for montante in meses:
    montante = capital * (1 + taxa) ** tempo
    print(montante)
'''




