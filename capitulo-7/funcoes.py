# def minha_func():
#     print('Minha primeira função!')
#
# minha_func()
# print(minha_func)
#
#
# a = 42
# def minha_funcao():
#
#     global a
#     a=35
#
# minha_funcao()
#
# print (a)
#

# RETORNO
#
# def area_circunferencia():
#         raio = float(input('Entre com o raio da circunferencia:'))
#         pi = 3.14
#
#         return pi * raio ** 2
#
# resultado=area_circunferencia()
#
# print(resultado)

#
def area_circunferencia():
    raio = float(input('Entre com o raio da circunferencia: '))
    pi = 3.14

    return f'{pi * raio ** 2} m²'


resultado = area_circunferencia()
#
# print(resultado)