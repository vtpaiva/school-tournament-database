from .functionalities.insert_estudante import insert_estudante
from .functionalities.insert_modalidade import insert_modalidade
from .functionalities.query import query_jogos

if __name__ == "__main__":
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Estudante")
        print("2. Cadastrar Modalidade")
        print("3. Consultar jogos")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")
        print('')
        
        if opcao == '1':
            insert_estudante()
        elif opcao == '2':
            insert_modalidade()
        elif opcao == '3':
            query_jogos()
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")