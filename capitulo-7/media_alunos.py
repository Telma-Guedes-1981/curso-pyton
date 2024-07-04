#
# alunos = {'João': [7,4,5], 'Maria': [5,8,9], 'Leo': [6,7,7], 'Pedro':[7,4,10]}
#
# alunos_medias = list(map(lambda notas: round(sum(notas) / len(notas), 2), alunos.values()))
#
# print(alunos_medias)
#
#
# def numeros_pares(num):
#     return num % 2 == 0
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# lista_pares = []
#
# for numero in lista:
#     if numeros_pares (numero):
#         lista_pares.append(numero)
#
#     print(lista_pares)


#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# lista_pares = list(filter(lambda x: x%2 == 0, lista))
#
# print (lista_pares)


# ALUNOS APROVADOS

alunos_notas = {'João': [7,4,5], 'Maria': [5,8,9], 'Leo': [6,7,7], 'Pedro':[7,4,10]}

alunos_aprovados = dict(filter(lambda alunos: round(sum(alunos[1]) / len(alunos[1]), 2) >= 7,
                               alunos_notas.items()))

print (alunos_aprovados)