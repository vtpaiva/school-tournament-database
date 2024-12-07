from psycopg.sql import SQL, Identifier

from . import *
from ..tabelas.modalidade import Modalidade


def inserir_modalidade_generico(modalidade, id, cursor):
    table_name = 'modalidade_desportiva' if modalidade.disability_type == "NENHUMA" else 'modalidade_paradesportiva'

    cursor.execute(
        SQL("INSERT INTO {} (ID) VALUES (%(id)s)").format(
            Identifier(table_name)),
        {'id': str(id[0])})


def inserir_tupla(modalidade, cursor):
    cursor.execute("""
        INSERT INTO Modalidade
            (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA,
                PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
        VALUES
            (%(sport)s, %(sex)s, %(min_age)s, %(max_age)s, %(height)s, %(weight)s,
            %(disability_type)s, %(n_start)s, %(n_reserve)s, %(scor_rule)s)
        RETURNING ID;
    """, {
        'sport': modalidade.sport,
        'sex': modalidade.sex,
        'min_age': modalidade.min_age,
        'max_age': modalidade.max_age,
        'height': modalidade.height,
        'weight': modalidade.weight,
        'disability_type': modalidade.disability_type,
        'n_start': modalidade.n_start,
        'n_reserve': modalidade.n_reserve,
        'scor_rule': modalidade.scor_rule
    })

    resultado_id = cursor.fetchone()

    if resultado_id is None:
        raise ValueError("Insertion error")

    inserir_modalidade_generico(
        modalidade=modalidade,
        id=resultado_id,
        cursor=cursor)


def inserir_modalidade():
    try:
        conn, cursor = conectar_banco()

        nova_tupla = Modalidade.get_from_input()

        inserir_tupla(modalidade=nova_tupla, cursor=cursor)

        conn.commit()

        print(f"Modalidade de {nova_tupla.sport} cadastrada com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir modalidade: {e}")

    finally:
        cursor.close()
        conn.close()
