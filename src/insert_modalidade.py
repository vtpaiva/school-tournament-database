from common.utils import conectar_banco
from tables.modalidade import Modalidade
from psycopg.sql import SQL

def insert_modalidade_generico(cursor, new_tuple, id):
    table_name = "Modalidade_Desportiva" if new_tuple.disability_type == "NENHUMA" else "Modalidade_Paradesportiva"

    cursor.execute(SQL(f"""
        INSERT INTO {table_name} 
            (ID)
        VALUES 
            (%s);
    """), (
        id[0],
    ))
    
def insert_modalidade(new_tuple, cursor):
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
        new_tuple.scor_rule,
    ))

    result_id = cursor.fetchone()

    if not result_id:
        raise ValueError("Insertion error")
    
    insert_modalidade_generico(cursor=cursor, new_tuple=new_tuple, id=result_id)

if __name__ == '__main__':
    try:
        conn, cursor = conectar_banco()

        dic = {
            'sport': 'XADREZ',
            'sex': 'M',
            'min_age': '2',
            'max_age': '4',
            'height': 'ALTO',
            'weight': 'LEVE',
            'disability': 'NENHUMA',
            'n_start': '11',
            'n_reserve': '5',
            'scor_rule': 'V1E0D0'
        }

        new_tuple = Modalidade.get_from_dict(dicti=dic)

        insert_modalidade(new_tuple=new_tuple, cursor=cursor)
        conn.commit()

    except Exception as error:
        print('Insertion error:', error)

        conn.rollback()

    finally:
        cursor.close()
        conn.close()