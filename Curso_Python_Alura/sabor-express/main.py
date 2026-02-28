import os

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

def ecolher_opcao():
    escolha_do_user = int(input('Escolha uma opção: '))

    match escolha_do_user:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurante')
        case 3:
            print('Ativar restaurante')
        case 4:
            finalizar_app()
    
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    ecolher_opcao()
    
if __name__ == '__main__':
    main()