#
# def bissexto(ano):
#
#     if(ano % 4==0 and ano % 100 !=0) or ano % 400 == 0:
#         print('É bissexto')
#
#     else:
#         print('Não é bissexto')
#
# bissexto(2000)
# bissexto(2001)

# def bissexto():
#     ano = int(input("Digite o ano: \n"))
#     if ano % 400 ==0:
#         print('É bissexto')
#     elif ano % 4 ==0:
#         if ano % 100!=0:
#             print('É bissexto')
#         else:
#             print('Não é bissexto')
#     else:
#         print('Não é bissexto')
# #
# # bissexto()
# #
# # def soma(a: int | None = 0; b: int | None = 0) -> int:
# #
# # """"""
#
# def notas_alunos(**kwargs: int |float):
#     for aluno, notas in kwargs.items():
#         print(f'{aluno} tirou {nota} na prova p1.')
#
#     return kwargs
#
# meus_alunos = notas_alunos(joao = 7, maria = 8.5)
# print (meus_alunos)


# def atualiza_estoque(**kwargs):
#     print('\n--------Vamos atualizar o estoque no sistema--------')
#     estoque = {}
#     for item, quantidade in kwargs.items():
#         estoque[item] = quantidade
#     print('\n--------Resumo do estoque--------\n')
#     if len(estoque) > 0:
#         for produto, quantidade, in estoque.items():
#             print(f' \nTemos um total de {sum(estoque.values())} produtos no estoque')
#         else:
#             print('0estoque está vazio')
#
# atualiza_estoque(banana = 2, maca = 3)


#EXPRESSOES LAMBDA - DESAFIO 9

kelvin = lambda ceulsius: ceulsius + 273.15

print(kelvin(0))


