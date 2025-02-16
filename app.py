import os

restaurantes = []

def menu():
    print(' ------ 𝚂𝚊𝚋𝚘𝚛𝚎𝚜 𝚎𝚡𝚙𝚛𝚎𝚜𝚜 ------- ')
    print('(1) - Cadastrar Restaurate')
    print('(2) - Listar Restaurantes')
    print('(3) - Alternar estado do Restaurante')
    print('(4) - SAIR \n')

def finalizar_app():
    os.system('cls')
    print('Finalizando aplicação...\n')

def opcao_invalida():
    print('Opção inválida!')
    voltar_menu()

def cadastro_restaurante():
    exibir_subtitulo('𝙲𝚊𝚍𝚊𝚜𝚝𝚛𝚘 𝚁𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎')
    nome_restaurante = str(input('Digite o nome do restaurante: '))
    catergoria = str(input('Digite a categoria do restaurante: '))

    rest = {
        "nome": nome_restaurante,
        "categoria": catergoria,
        "situacao": False
    }

    restaurantes.append(rest)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()


def nenhum_restaurante():
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado!')
        voltar_menu()    

def listar_restaurantes():
    exibir_subtitulo('𝙻𝚒𝚜𝚝𝚊𝚛 𝚁𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎𝚜')

    nenhum_restaurante()
    if len(restaurantes) > 0:
        linha = '-' * 70
        print(f'{'Nome do restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | {'Situação'}')
        print(linha) 
        for i, rest in enumerate(restaurantes, start=1):
            nome = rest['nome']
            categoria = rest['categoria']
            situação = 'Ativado' if rest['situacao'] else 'Desativado'
            print(f'{i} - {nome.ljust(20)} | {categoria.ljust(20)} | {situação}')
            voltar_menu()

def alterar_situacao_restaurante():
    exibir_subtitulo('Alternando o estado do 𝚁𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎')

    nenhum_restaurante()
    if len(restaurantes) > 0:
        nome_restaurante = str(input('Digite o nome do restaurante que deseja alternar o estado: '))
        restaurante_encontrado =  False

        for rest in restaurantes:
            if rest['nome'] == nome_restaurante:
                restaurante_encontrado = True
                rest['situacao'] = not rest['situacao']
                msg =  f'O restaurante {nome_restaurante} foi ativado' if rest['situacao'] else f'O restaurante {nome_restaurante} foi desativado'
                print(msg)
        if not restaurante_encontrado:
            print(f'O restaurante {nome_restaurante} não foi encontrado!')         
        voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto) * 2)
    print(linha)
    print(texto)
    print(linha)

def voltar_menu():
    input('\nDigite qualquer tecla para voltar ao menu...')
    main()    

def escolher_opcao():
    try:
        op = int(input('Digite a opção desejada: '))
        match op:
            case 1:
                cadastro_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_situacao_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
        