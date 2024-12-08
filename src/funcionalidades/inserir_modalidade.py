from psycopg.sql import SQL, Identifier

from . import *
from ..tabelas.modalidade import Modalidade


# Função que insere uma modalidade específica na tabela 'modalidade_desportiva' ou 'modalidade_paradesportiva'
def inserir_modalidade_generico(modalidade: Modalidade, id: int, cursor: object) -> None:
    """
    Insere uma entrada genérica em uma das tabelas de modalidade ('modalidade_desportiva' ou 'modalidade_paradesportiva').

    Parâmetros:
        modalidade (Modalidade): Objeto que contém os dados da modalidade.
        id (tuple): ID da modalidade gerado pelo banco de dados.
        cursor (object): Cursor para executar as consultas SQL no banco de dados.
    """

    nome_tabela = 'modalidade_desportiva' if modalidade.deficiencia == "NENHUMA" else 'modalidade_paradesportiva'

    cursor.execute(
        SQL("INSERT INTO {} (ID) VALUES (%(id)s)").format(Identifier(nome_tabela)),
        {'id': str(id[0])}  # Insere o ID gerado anteriormente
    )


# Função que insere uma nova tupla de modalidade na tabela 'Modalidade' e depois associa a uma tabela de modalidade específica
def inserir_tupla(modalidade: Modalidade, cursor: object) -> None:
    """
    Insere uma nova tupla de modalidade na tabela 'Modalidade' e associa a uma das tabelas 'modalidade_desportiva' ou 'modalidade_paradesportiva'.

    Parâmetros:
        modalidade (Modalidade): Objeto que contém os dados da modalidade.
        cursor (object): Cursor para executar as consultas SQL no banco de dados.

    Exceções:
        ValueError: Levantada se a consulta INSERT não retornar o ID da modalidade.
    """

    cursor.execute("""
        INSERT INTO Modalidade
            (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA, PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
        VALUES
            (%(sport)s, %(sex)s, %(min_age)s, %(max_age)s, %(height)s, %(weight)s, %(disability_type)s, %(n_start)s, %(n_reserve)s, %(scor_rule)s)
        RETURNING ID;
    """, {
        'sport': modalidade.esporte, 
        'sex': modalidade.sexo, 
        'min_age': modalidade.idade_min,  
        'max_age': modalidade.idade_max, 
        'height': modalidade.altura, 
        'weight': modalidade.peso, 
        'disability_type': modalidade.deficiencia, 
        'n_start': modalidade.n_titulares,  
        'n_reserve': modalidade.n_reservas,  
        'scor_rule': modalidade.regra_pont  
    })

    resultado_id = cursor.fetchone()

    if resultado_id is None:
        raise ValueError("Erro ao inserir modalidade, nenhum ID retornado.")

    inserir_modalidade_generico(
        modalidade=modalidade,
        id=resultado_id,
        cursor=cursor
    )


# Função principal que gerencia a inserção de uma nova modalidade no banco de dados
def inserir_modalidade() -> None:
    """
    Gerencia o processo de entrada de dados, criação de uma nova modalidade e inserção no banco de dados.

    Passos:
    1. Conecta ao banco de dados.
    2. Coleta as informações da modalidade a partir da entrada do usuário.
    3. Insere as informações na tabela 'Modalidade' e nas tabelas específicas ('modalidade_desportiva' ou 'modalidade_paradesportiva').
    4. Exibe uma mensagem de sucesso ou erro.
    5. Fecha a conexão com o banco, independentemente de sucesso ou erro.
    """

    try:
        conn, cursor = conectar_banco()

        nova_tupla = Modalidade.get_from_input()

        inserir_tupla(modalidade=nova_tupla, cursor=cursor)

        cursor.close()
        conn.commit()

        print(f"\nModalidade de {nova_tupla.esporte} cadastrada com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"\nErro ao inserir modalidade: {e}")

    finally:
        conn.close()
