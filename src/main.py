from .funcionalidades.consulta_jogos import consultar_jogos
from .funcionalidades.inserir_estudante import inserir_estudante
from .funcionalidades.inserir_modalidade import inserir_modalidade

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
            inserir_estudante()
        elif opcao == '2':
            inserir_modalidade()
        elif opcao == '3':
            consultar_jogos()
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")
