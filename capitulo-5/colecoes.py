# #
# # print(ord('c'))
# # print(ord('C'))
# #
# #
# # minha_lista = [1,2,3,4,5]
# #
# # print(minha_lista)
# # print(type(minha_lista))
# #
# # print(type(minha_lista[2])
# # print(type(minha_lista[1])
# # print(type(minha_lista[-1])
# #
#
# nome = 'Thiago'
#
# print(nome[-1])
#
# # # Slicing
# #
# # print(minha_lista[0:4])
# #
# # minha_lista_2 = list(range(1,21))
# #
# # print(minha_lista_2)
# #
# # print(minha_lista_2[1:12:2])
# #
# # print(sum(minha_lista_2))
# # print(max(minha_lista_2))
# # print(min(minha_lista_2))
#
# # Métodos
#
# minha_lista_2 = list(range(1,11))
# print(minha_lista_2)
#
# minha_lista_2.append(11)
#
# print(minha_lista_2)
#
# minha_lista_2.append([12,13,14])
# print(minha_lista_2)
#
# minha_lista_2.extend([12,13,14])
# print(minha_lista_2)


nome_completo = []

while True:

    nome=input('Adiciona um nome(ou enter para sair):').title()
    nome_completo.append(nome)

    if not nome:

        nome_completo = ''.join(nome_completo)
        break

    print(nome_completo)
















