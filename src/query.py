from common.utils import conectar_banco

def query_modalidade(cursor):
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
            EQUIPE E ON D.ID_EQUIPE = E.ID AND E.ID = %s
        JOIN
            JOGO J ON J.ID = D.ID_JOGO AND EXTRACT(YEAR FROM J.DATA_JOGO) = %s
        RIGHT JOIN
            PossiveisResultados P ON P.RESULTADO = D.RESULTADO
        GROUP BY
            P.RESULTADO
        ORDER BY
            P.RESULTADO DESC;
        """, (
            team_id,
            year,
        ))

if __name__ == '__main__':
    try:
        conn, cursor = conectar_banco()

        query_modalidade(cursor=cursor)
        
        resultados = cursor.fetchall()

        for row in resultados:
            print(row)

    except Exception as error:
        print('Query error: ', error)

    finally:
        cursor.close()
        conn.close()