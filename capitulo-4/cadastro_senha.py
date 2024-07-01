
senha = input('Cadastre uma senha de 6: \n')


print(len(senha))

while len(senha)!= 6:
    senha = input('quantidade de char invalida \n'
                  'Cadastre uma senha de 6: \n')

print('Cadastro realizado com sucesso')


listas_acessos = ['1thiago_001','chave_1','chave_2']
controle_acesso = False

while not controle_acesso:
    chave_acesso = input('informe sua credencial')

    if chave_acesso in listas_acessos:

        controle_acesso = True

    else:
        continue
print('\nBem-vindo ao sistema.')


