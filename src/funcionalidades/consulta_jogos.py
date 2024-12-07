from . import *


# Função que verifica se não houve jogos no período consultado
def sem_jogos_no_periodo(resultados):
    """
    Verifica se não houve jogos no período consultado.

    Parâmetros:
        resultados (list of tuples): Lista de tuplas com o resultado e o total de jogos por tipo de resultado.

    Retorno:
        bool: True se o total de jogos for zero para todos os tipos de resultado, False caso contrário.
    """
    return all(tupla[1] == 0 for tupla in resultados)


# Função que executa a consulta de jogos de uma equipe em um determinado ano
def selecionar_jogos(cursor):
    """
    Executa a consulta de jogos de uma equipe em um determinado ano.

    Parâmetros:
        cursor (object): Cursor para executar a consulta SQL no banco de dados.

    Exceções:
        ValueError: Levantada se o ID do time ou o ano forem menores que 1.
    """
    time_id = input("Digite o ID do time a ser consultado: ")
    if int(time_id) < 1:
        raise ValueError("O ID da equipe deve ser maior que zero.")

    ano_consulta = input("Digite o ano de jogos a ser consultado: ")
    if int(ano_consulta) < 1:
        raise ValueError("O ano deve ser maior que zero.")

    cursor.execute("""
        SELECT
            P.RESULTADO,
            COUNT(Subquery.ID) AS TOTAL
        FROM (
            SELECT 'V'::RESULTADO_JOGO AS RESULTADO
            UNION ALL
            SELECT 'D'::RESULTADO_JOGO
            UNION ALL
            SELECT 'E'::RESULTADO_JOGO
            UNION ALL
            SELECT 'P'::RESULTADO_JOGO
        ) AS P
        LEFT JOIN (
            SELECT
                D.RESULTADO,
                E.ID
            FROM
                DISPUTA D
            JOIN
                EQUIPE E ON D.ID_EQUIPE = E.ID
            JOIN
                JOGO J ON J.ID = D.ID_JOGO
            WHERE
                E.ID = %(id)s
                AND EXTRACT(YEAR FROM J.DATA_JOGO) = %(ano)s
        ) AS Subquery
        ON P.RESULTADO = Subquery.RESULTADO
        GROUP BY
            P.RESULTADO
        ORDER BY
            P.RESULTADO DESC;
        """, {
        'id': time_id,
        'ano': ano_consulta,
    })


# Função que realiza a consulta de jogos de uma equipe e exibe os resultados
def consultar_jogos():
    """
    Conecta ao banco de dados, consulta os jogos de uma equipe em um ano específico e exibe os resultados.

    Caso não haja jogos registrados para o ano e equipe informados, uma mensagem de aviso será exibida.
    Em caso de erro na consulta, o erro será exibido e a transação será revertida.

    Exceções:
        Exception: Captura qualquer exceção gerada durante o processo de consulta.
    """
    try:
        conn, cursor = conectar_banco()

        selecionar_jogos(cursor=cursor)

        resultados = cursor.fetchall()

        cursor.close()
        conn.commit()

        # Exibe os resultados dos jogos
        for tupla in resultados:
            print(tupla)

        if sem_jogos_no_periodo(resultados=resultados):
            print(
                '\nWARNING: A equipe não existe ou não jogou nenhum jogo no ano consultado.')

    except Exception as e:
        conn.rollback()
        print(f"Erro ao consultar jogos: {e}")

    finally:
        conn.close()