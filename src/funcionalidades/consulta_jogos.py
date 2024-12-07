from . import *


def sem_jogos_no_periodo(resultados):
    return all(tupla[1] == 0 for tupla in resultados)


def selecionar_jogos(cursor):
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


def consultar_jogos():
    try:
        conn, cursor = conectar_banco()

        selecionar_jogos(cursor=cursor)

        resultados = cursor.fetchall()

        cursor.close()
        conn.commit()

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