
senha = input('Cadastre uma senha de 6: \n')

while True:

    if len(senha) != 6:
        senha = input('Quantidade de char invalida \n'
                     'Cadastre uma senha de 6: \n')
        continue

    else:
        break

print('senha cadastrada com sucesso')

listas_acessos = ['thiago_001','chave_1','chave_2']
controle_acesso = False

while not controle_acesso:
    chave_acesso = input('informe sua credencial: \n')

    if chave_acesso in listas_acessos:

        controle_acesso = True

    else:
        continue
print('\nBem-vindo ao sistema.')

