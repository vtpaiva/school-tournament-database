import psycopg
from utils.modalidade import Modalidade

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
            a = Modalidade.get_from_input()

            cursor.execute("""
                INSERT INTO Modalidade 
                    (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA, 
                        PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
                VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING ID;
            """, (
                a.sport, 
                a.sex, 
                a.min_age, 
                a.max_age, 
                a.height, 
                a.weight, 
                a.disability_type, 
                a.n_start, 
                a.n_reserve, 
                a.scor_rule
            ))

            result_id = cursor.fetchone()

            table_name = "Modalidade_Desportiva" if a.disability_type == "NENHUMA" else "Modalidade_Paradesportiva"

            cursor.execute(f"""
                INSERT INTO {table_name} 
                    (ID)
                VALUES 
                    ({result_id[0]});
            """
            )

            conn.commit()

        except Exception as error:
            print('Insertion error:', error)

            conn.rollback()