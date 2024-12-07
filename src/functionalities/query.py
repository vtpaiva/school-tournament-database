from . import *

def has_no_games_played(resultados):
    return all(row[1] == 0 for row in resultados)

def query(cursor):
    team_id = input("Team? ")
    if int(team_id) < 1:
        raise ValueError("ID deve ser maior que um")

    year = input("Year? ")           
    if int(year) < 0:
        raise ValueError("Ano deve ser maior que zero") 

    cursor.execute("""
        WITH PossiveisResultados AS (
            SELECT 'V'::RESULTADO_JOGO AS RESULTADO
            UNION ALL
            SELECT 'D'::RESULTADO_JOGO
            UNION ALL
            SELECT 'E'::RESULTADO_JOGO
            UNION ALL
            SELECT 'P'::RESULTADO_JOGO
        )

        SELECT
            P.RESULTADO,
            COUNT(E.ID)
        FROM
            DISPUTA D
        JOIN
            EQUIPE E ON D.ID_EQUIPE = E.ID AND E.ID = %(id)s
        JOIN
            JOGO J ON J.ID = D.ID_JOGO AND EXTRACT(YEAR FROM J.DATA_JOGO) = %(year)s
        RIGHT JOIN
            PossiveisResultados P ON P.RESULTADO = D.RESULTADO
        GROUP BY
            P.RESULTADO
        ORDER BY
            P.RESULTADO DESC;
        """, {
            'id': team_id,
            'year': year,
        })

def query_jogos():
    try:
        conn, cursor = conectar_banco()

        query(cursor=cursor)
        
        resultados = cursor.fetchall()

        cursor.close()
        conn.commit()

        for row in resultados:
            print(row)

        if has_no_games_played(resultados=resultados):
            print('\nWARNING: A equipe não existe ou não jogou nenhum jogo no ano consultado.')

    except Exception as error:
        conn.rollback()

        print('Query error: ', error)

    finally:
        conn.close()