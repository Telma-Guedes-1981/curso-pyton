
sol = False
calor = False

if sol and calor:
    print('Bora para praia!')

elif sol and not calor:
    print('Bora para o parque!')

elif not sol and calor:
    print('Bora para piscina')

elif not sol and not calor:
    print('netflix?')



# DESAFIO
a = int(input('A'))
b = int(input('B'))
c = int(input('C'))

if (a+b>c) or (b+c>a) or (a+c>b):
    print('É um triangulo')

if (a == b == c):
    print('equilatero')

elif a == b or b == c or a == c:
    print('isósceles')

elif a != b or b != c or a != c:
    print('escaleno')






