nota1= int(input("Insira a primeira nota: "))
nota2= int(input("Insira a segunda nota: "))

media = ((nota1 + nota2) / 2)

print('A média das duas notas é ', media)
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
