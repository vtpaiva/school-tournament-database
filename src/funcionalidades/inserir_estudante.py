from . import *
from ..tabelas.estudante import Estudante


# Função que insere um registro de estudante na tabela 'Estudante' e 'Funcoes'
def inserir_tupla(estudante: Estudante, cursor: object) -> None:
    """
    Insere uma tupla de estudante no banco de dados.

    Parâmetros:
        estudante (Estudante): Objeto da classe Estudante com os dados do estudante.
        cursor (object): Cursor para executar as consultas SQL no banco de dados.
    """
    
    # Insere o CPF do estudante na tabela genérica de funções
    inserir_funcao(estudante.cpf, cursor)

    cursor.execute("""
        INSERT INTO Estudante (CPF, NOME, ALTURA, PESO, SEXO, IDADE, TIPO_DEFICIENCIA)
        VALUES (%(cpf)s, %(nome)s, %(altura)s, %(peso)s, %(sexo)s, %(idade)s, %(deficiencia)s)
    """, {
        'cpf': estudante.cpf,  
        'nome': estudante.nome,  
        'altura': estudante.altura, 
        'peso': estudante.peso,  
        'sexo': estudante.sexo, 
        'idade': estudante.idade,  
        'deficiencia': estudante.deficiencia  
    })


# Função que insere uma função associada ao CPF na tabela 'Funcoes'
def inserir_funcao(cpf: str, cursor: object) -> None:
    """
    Insere uma entrada de função na tabela 'Funcoes'.

    Parâmetros:
        cursor (object): Cursor para executar as consultas SQL no banco de dados.
        cpf (str): CPF do estudante para o qual a função será associada.
    """

    cursor.execute("""
        INSERT INTO Funcoes (CPF, FUNCAO)
        VALUES (%(cpf)s, 'E')
    """, {'cpf': cpf})


# Função principal que gerencia a inserção de um novo estudante no banco de dados
def inserir_estudante() -> None:
    """
    Gerencia o processo de entrada de dados, criação de um novo estudante e inserção no banco.

    Passos:
    1. Conecta ao banco de dados.
    2. Coleta as informações do estudante a partir da entrada do usuário.
    3. Insere as informações na tabela 'Estudante' e 'Funcoes'.
    4. Exibe uma mensagem de sucesso ou erro.
    5. Fecha a conexão com o banco, independentemente de sucesso ou erro.
    """

    try:
        conn, cursor = conectar_banco()

        nova_tupla = Estudante.get_from_input()

        inserir_tupla(estudante=nova_tupla, cursor=cursor)

        cursor.close()
        conn.commit()

        print(f"\nEstudante {nova_tupla.nome} cadastrado com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"\nErro ao inserir estudante: {e}")

    finally:
        conn.close()
