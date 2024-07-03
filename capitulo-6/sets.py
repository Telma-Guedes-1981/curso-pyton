# #
# # s1 = {1, 2, 3, 4, 5}
# #
# # print(s1)
# # print(type(s1))
# #
# # s2 = {4, 5, 6, 7, 8}
# #
# # print(s2)
# #
# # u = s1.union(s2)
# # print(u)
# #
# # i = s1.intersection(s2)
# # print(i)
# #
# # s1.add('item novo')
# # print(s1)
# #
# # d = s1.difference(s2)
# # print(d)
# #
# # print(sum
#
#
# #DESAFIO 5
#

#
# lista = []
#
# while True:
#
# int(input('Digite o numero (ou enter para sair:'))
#
# if item:
# print(lista)
# s1.intersection(lista)
#

# s1 = {1, 2, 3, 4, 5}
# print(sorted(s1))
#

# s1 = {1, 2, 3, 4, 5}
# print(s1)


#solução b

s = set()

while True:

    item = input('Digite o numero (ou enter para sair:')
    if item:
        s.add(int(item))
        continue
    else:
        break

lista_final = list(sorted(s))

print(lista_final)





