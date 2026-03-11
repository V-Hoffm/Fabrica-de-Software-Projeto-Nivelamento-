from Banco import consulta_locais, salvar_solicitacao, salvar_denuncia, salvar_review # faz o import de todas as funções para realizar as operações no banco
from datetime import datetime # importa função datetime da biblioteca datetime

def exibir_menu(): # construção do menu inicial com as opções para serem selecionadas
    print("\n" + "="*30)
    print("             MENU")
    print("="*30)
    print("1 -- Menu Inicial")
    print("2 -- Consulta de Locais")
    print("3 -- Solicitar Coleta")
    print("4 -- Denúncias")
    print("5 -- Suporte e Reviews")
    print("0 -- Sair")
    print("="*30)

while True: # while true para o código ficar rodando e eu poder selecionar as opções e não fechar tudo após realizar alguma ação
    exibir_menu() # chamo a função menu
    try: # utilizo try para tratamento de erros caso usuário escreva algo que não é um número
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: Digite apenas números.") # texto que será retornado caso o usuário digite uma str ( está aqui para direcionar o usuário corretamente )
        continue

    if opcao == 0:
        print("Encerrando sistema...") # opção 0 com um break para finalizar tudo e sair do sistema
        break

    elif opcao == 1:
        continue # volta automáticamente para o menu inicial

    elif opcao == 2: # opção para realizar a consulta dos locais
        cidade = input("Cidade para consulta: ").lower().strip() # input com lower e strip para deixar tudo minusculo e remover espaços em branco no inicio e final para não dar divergencia com o banco
        while True:
            print("\nEscolha o tipo de objeto:")
            print("1 - Baterias")
            print("2 - Eletrônicos")
            print("3 - Plástico")
            print("4 - Vidro")
            print("5 - Papel")
            print("6 - Metal")
            print("7 - Óleo")
            opcoes = ["baterias", "eletrônicos", "plástico", "vidro", "papel", "metal", "óleo" ]
            escolha = int(input("-> ")) - 1
            try:
                objeto = opcoes[escolha]
                print(objeto)
                break
            except IndexError:
                print("Número não cadastrado como opções")
            except ValueError:
                print("Por favor, digite um número válido.")
        print(f"\nBuscando pontos de descarte em {cidade} para {objeto}...") # texto apenas para mostrar ao usuário que estamos buscando os locais
        locais = consulta_locais(cidade, objeto) # variavel locais que recebe uma lista de tuplas da função consulta_locais
        if locais: # verifica se a lista tem alguma dupla se for True ele entra no if e printa todos os itens
            for l in locais: print(f"-> {l}") # faz um print de cada tupla de dentro da lista, cada tupla é uma linha do banco
        else: # se não encontra nada ele retorna um texto
            print("Nenhum ponto encontrado com esses critérios.")

    elif opcao == 3:
        nome = input("Seu nome: ")
        obj = input("Tipo de objeto para coleta: ")
        local = input("Endereço de coleta: ")
        while True: # um while true para possibilitar o usuário de avançar apenas caso o usuário informe corretamente o período
            print("\nEscolha o período:")
            print("1 - Matutino")
            print("2 - Vespertino")
            
            escolha = input("-> ") # if para verificar se o usuário digitou corretamente
            if escolha == "1":
                periodo = "Matutino"
                break 
            elif escolha == "2":
                periodo = "Vespertino"
                break
            else:
                print("Opção inválida! Por favor, digite 1 para Matutino ou 2 para Vespertino.") # else que informa ao usuário o caminho a seguir e volta novamente para a pergunta

        salvar_solicitacao(nome, obj, local, periodo) # chama a função para fazer um insert dentro da tabela no banco de dados
        print("\n Solicitação de coleta cadastrada com sucesso!") # informa o usuário que a sua solicitação foi cadastrada

    elif opcao == 4:
        loc = input("Local da irregularidade: ")
        while True: # um while true para que o usuário só consiga progredir se ele informar corretamente a data e hora
            data_hora = input("Informe a data e horário (Ex: 10/03/2026 14:30): ") # data hora com exemplo
            try: # try para tratamento de erros caso o usuário digite algo que não é aceito como data
                hor = datetime.strptime(data_hora, "%d/%m/%Y %H:%M") #função que pega a str e passa para data no formato dia mes ano hora minuto
            
                if hor > datetime.now(): # if para validar se o usuário não está digitando uma data no futuro
                    print("A data não pode ser no futuro!")
                    continue
                break # caso não caia no except e nem no if ele da um break no while
            except ValueError:
                print("Formato inválido! Use o padrão: DIA/MES/ANO HORA:MIN (Ex: 10/03/2026 14:30)") #caso o usuario erre é lançado um except

        img = input("Caminho/Link da imagem da denúncia: ")
        descricao = input("Deixe uma descrição do acontecido: ")
        
        salvar_denuncia(loc, hor, img, descricao)
        print("\n Denúncia registrada. Obrigado por ajudar o meio ambiente!")

    elif opcao == 5: # opção 5 que irá passar para os usuários as informações para suporte e review
        print("\n--- SUPORTE ---")
        print("E-mail: suporte@eco.com.br | Tel: (47) 9999-9999")
        print("\n--- DEIXE UM REVIEW ---")
        coment = input("Seu comentário: ")
        salvar_review(coment) # função para guardar a review dentro do banco de dados
        print("Obrigado pelo seu feedback!")

    else:
        print("Opção inválida!") # else para caso o usuário digite um número errado dentro do menu