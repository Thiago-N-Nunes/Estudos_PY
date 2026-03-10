import os

restaurantes = [{'nome' : 'Pizzaria Estrela','categoria' : 'Italiano', 
                 'inaugurado' : False}, 
                {'nome' : 'Gojou Restaurante','categoria' : 'Japonesa','inaugurado' : True}]

def exibir_nome_do_programa():
    print("""🅂🄰🄱🄾🅁 🄴🅇🄿🅁🄴🅂🅂""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app(): 
    exibir_subtitulo('APP FINALIZADO')
    voltar_menu()

def voltar_menu():
    input('Digite uma tecla pra voltar pro menu principal')
    main()

def opcao_invalida():
    print("Opção Invalida")
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print (texto)
    print()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRO DE NOVO RESTAURANTE')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria' : categoria, 'inaugurado' : False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = restaurante['inaugurado']
        print(f' - {nome_restaurante} | {categoria} | {status}')
        
    
    voltar_menu()

def ativar_restaurante():
    exibir_subtitulo('ALTERNANDO STATUS RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['inaugurado'] = not restaurante['inaugurado']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['inaugurado'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado')
            
    voltar_menu()

def ecolher_opcao():
    try:
        escolha_do_user = int(input('Escolha uma opção: '))

        match escolha_do_user: 
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:            
                ativar_restaurante()
            case 4:
                finalizar_app()   
    except:
        opcao_invalida()    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    ecolher_opcao()
    
if __name__ == '__main__':
    main()