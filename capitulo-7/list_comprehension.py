#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# lista_2 = [n * 2 for n in lista]
#
# # print (lista)
#
# print(lista_2)
#
# alunos_notas = {'João': [7,4,5], 'Maria': [5,8,9], 'Leo': [6,7,7], 'Pedro':[7,4,10]}
# #
# # medias = (round(sum(n))/len(n),2) for n in alunos_notas.values()]
# #     print(n)
# #
#
#
# lista_dezenas = [x * 10 for x in range(1,11)]
#
# print(lista_dezenas)
#
# tabuada_sete = (7 * x for x in range (1,11))
#
# print(*tabuada_sete, sep='\n')


# LIST_COMPREHENSION 2

lista_pares = {n for n in range(0,51) if n % 2 == 0}
print (lista_pares)

alunos_notas = {'João': [7,4,5], 'Maria': [5,8,9], 'Leo': [6,7,7], 'Pedro':[7,4,10]}

aprovados=(aluno[0] for aluno in alunos_notas.items()if round(sum(aluno[1]/len(aluno [1]),2 >= 7)

print(aprovados)



