#TAREFA: 
#    Um novo modelo de carro, super econômico foi lançado.
#    Ele faz 20 km com 1 litro de combustível.
#    Cada litro de combustível custa R$ 5,00.
#    Faça um programa que pergunte ao usuário quanto de dinheiro ele tem,
#    e em seguida diga quantos litros de combustível ele pode comprar
#    e quantos kilometros o carro consegue andar com este tanto de combustível.
#
#    1- Perguntar quanto dinheiro a pessoa tem:
#    2- Descobrir quantos litros ela pode comprar:
#    3- Descobrir quantos km dá pra rodar com isso:
#    ___________________________________________________________________________
    
#Entrada: 

dinheiro = input("Digite quanto dinheiro você tem agora: ")
preco = 5

#Processamento:

litros = int(float(dinheiro) / float(dinheiro))
distancia = int(litros) * 20

#Saída: 

print("Você pode abastecer " + str(litros) + "L.")
print("Você pode percorrer uma distância de " + str(distancia) + " km.")
