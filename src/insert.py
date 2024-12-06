from . import *
from utils.modalidade import Modalidade

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
                new_tuple = Modalidade.get_from_input()

                cursor.execute("""
                    INSERT INTO Modalidade 
                        (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA, 
                            PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
                    VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING ID;
                """, (
                    new_tuple.sport, 
                    new_tuple.sex, 
                    new_tuple.min_age, 
                    new_tuple.max_age, 
                    new_tuple.height, 
                    new_tuple.weight, 
                    new_tuple.disability_type, 
                    new_tuple.n_start, 
                    new_tuple.n_reserve, 
                    new_tuple.scor_rule
                ))

                result_id = cursor.fetchone()

                if not result_id:
                    raise ValueError("Insertion error")

                table_name = "Modalidade_Desportiva" if new_tuple.disability_type == "NENHUMA" else "Modalidade_Paradesportiva"

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