import random

numero_secreto= random.randint(0,100)
numero= int(input('digite um numero entre 0 a 100: \n'))

while numero != numero_secreto:
    print('você erro!')
    if numero > numero_secreto:
        print(f"o numero {numero} esta acima do numero secreto")
    else:
        print(f"o numero {numero} esta abaixo do numero secreto")

    numero= int(input('digite um numero entre 0 a 100: \n'))

print('parabens, você acerto! \n o numero secreto é {}'.format(numero_secreto))
print('fim com a tag')