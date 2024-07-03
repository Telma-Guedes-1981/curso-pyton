
estoque = {}
print(type(estoque))
print('\n--------Vamos atualizar o estoquer no sistema--------')
while True:
    produto = input('informe o nome do produto (ou enter para sair): ')
    if produto:
        quantidade = int(input(f'Quanto de {produto} temos em estoque: '))
        estoque[produto] = quantidade
        continue
    else:
        break
print('\n--------Resumo do estoque--------\n')
if len(estoque) > 0:
    for produto, quantidade in estoque.items():
        print(f'{produto}: {quantidade}: unidades.')
    print(f'\nTe,os um total de {sum(list(estoque.values()))} produtos no estoque.')
else:
    print('0 estoque está vazio.')



