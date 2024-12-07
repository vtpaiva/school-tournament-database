from . import *
from psycopg.sql import SQL, Identifier
from ..tables.modalidade import Modalidade

def insert_modalidade_generico(cursor, new_tuple, id):
    table_name = 'modalidade_desportiva' if new_tuple.disability_type == "NENHUMA" else 'modalidade_paradesportiva'

    cursor.execute(
        SQL("INSERT INTO {} (ID) VALUES (%(id)s)").format(Identifier(table_name)),
        {'id': str(id[0])})
    
def insert_modalidade(new_tuple, cursor):
    cursor.execute("""
        INSERT INTO Modalidade 
            (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA, 
                PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
        VALUES 
            (%(sport)s, %(sex)s, %(min_age)s, %(max_age)s, %(height)s, %(weight)s, 
            %(disability_type)s, %(n_start)s, %(n_reserve)s, %(scor_rule)s)
        RETURNING ID;
    """, {
        'sport': new_tuple.sport, 
        'sex': new_tuple.sex, 
        'min_age': new_tuple.min_age, 
        'max_age': new_tuple.max_age, 
        'height': new_tuple.height, 
        'weight': new_tuple.weight, 
        'disability_type': new_tuple.disability_type, 
        'n_start': new_tuple.n_start, 
        'n_reserve': new_tuple.n_reserve, 
        'scor_rule': new_tuple.scor_rule
    })

    result_id = cursor.fetchone()

    if not result_id:
        raise ValueError("Insertion error")
    
    insert_modalidade_generico(cursor=cursor, new_tuple=new_tuple, id=result_id)

def insert_modalidade():
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

        print(f"Modalidade de {new_tuple.sport} cadastrada com sucesso!")

    except Exception as error:
        print('Insertion error:', error)

        conn.rollback()

    finally:
        cursor.close()
        conn.close()