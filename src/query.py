from . import *

if __name__ == '__main__':
    conn_params = {
        'dbname': 'your_db',
        'user': 'your_user',  
        'host': 'localhost',     
        'password': 'your_password',
        'port': 5432             
    }

    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cursor:

            try:

                team_id = input("Team? ")
                year = input("Year? ")

                cursor.execute(f"""
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
                        EQUIPE E ON D.ID_EQUIPE = E.ID AND E.ID = {team_id}
                    JOIN
                        JOGO J ON J.ID = D.ID_JOGO AND EXTRACT(YEAR FROM J.DATA_JOGO) = {year}
                    RIGHT JOIN
                        PossiveisResultados P ON P.RESULTADO = D.RESULTADO
                    GROUP BY
                        P.RESULTADO
                    ORDER BY
                        P.RESULTADO DESC;
                    """)
                
                resultados = cursor.fetchall()

                for row in resultados:
                    print(row)

            except Exception as error:
                print('Query error:', error)