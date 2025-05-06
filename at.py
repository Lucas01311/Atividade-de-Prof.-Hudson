import time

bd_filmes = [
    ['Django', 2012],
    ['Velozes e Furiosos', 2002],
    ['Liga da Justiça', 1998]
]

def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i + 1} - {bd[i][1]} - {bd[i][0]}')

def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def alterar_filme(bd):
    print('\n--- Alterar Filme ---')
    for i, filme in enumerate(bd):
        print(f'{i + 1} - {filme[0]} ({filme[1]})')
    
    try:
        idx = int(input('Digite o número do filme que deseja alterar: ')) - 1
        if 0 <= idx < len(bd):
            novo_nome = input('Novo nome do filme: ')
            novo_ano = int(input('Novo ano do filme: '))
            bd[idx] = [novo_nome, novo_ano]
            print('Filme alterado com sucesso!')
        else:
            print('Número inválido! Nenhum filme foi alterado.')
    except ValueError:
        print('Entrada inválida! Use apenas números.')
    except Exception as e:
        print(f'Erro inesperado: {e}')

while True:
    print('\nBem-vindo ao FilmeBom')
    print('1 - Cadastrar filme')
    print('2 - Alterar filme')
    print('3 - Listar filmes')
    print('0 - Sair')

    try:
        op = int(input('Digite a opção desejada: '))
        time.sleep(1)
    except Exception as e:
        print(f'Erro: {e}')
        op = -1

    if op == 1:
        print(f'\n--- Cadastro de Filme ---')
        titulo = input('Digite o título do novo filme: ')
        try:
            ano = int(input('Digite o ano do novo filme: '))
            bd_filmes = cadastrar_filme(bd_filmes, titulo, ano)
            print('Filme cadastrado com sucesso!')
        except ValueError:
            print('Ano inválido. Tente novamente.')
        
    elif op == 2:
        alterar_filme(bd_filmes)

    elif op == 3:
        print('\n--- Lista de Filmes ---')
        listar_filmes(bd_filmes)

    elif op == 0:
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida! Tente novamente!')

    time.sleep(2)