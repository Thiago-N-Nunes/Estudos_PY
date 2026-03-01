import os
restaurantes = []

def exibir_nome_do_programa():
    print("""🅂🄰🄱🄾🅁 🄴🅇🄿🅁🄴🅂🅂""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizou app\n')

def opcao_invalida():
    print("Opção Invalida")
    input('Digite uma tecla pra voltar pro menu principal')
    main()
    
def cadastrar_novo_restaurante():
    os.system('cls')
    print('CADASTRO DE NOVOS RESTAUTANTES')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla pra voltar ao menu principal')
    main()

def ecolher_opcao():
    try:
        escolha_do_user = int(input('Escolha uma opção: '))

        match escolha_do_user: 
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                print('Listar restaurante')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()    
    except:
        opcao_invalida()    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    ecolher_opcao()
    
if __name__ == '__main__':
    main()