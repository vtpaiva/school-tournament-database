from . import *
from ..tables.estudante import Estudante

def inserir_estudante(conn, cursor, student):
    inserir_funcao(cursor, student.cpf, 'E')

    cursor.execute("""
        INSERT INTO Estudante (CPF, NOME, ALTURA, PESO, SEXO, IDADE, TIPO_DEFICIENCIA)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (student.cpf, 
          student.nome, 
          student.altura, 
          student.peso, 
          student.sexo, 
          student.idade, 
          student.deficiencia,))

def inserir_funcao(cursor, cpf, funcao):
    cursor.execute("""
        INSERT INTO Funcoes (CPF, FUNCAO)
        VALUES (%s, %s)
    """, (cpf, funcao,))

def insert_estudante():
    try:
        conn, cursor = conectar_banco()

        dic = {
            'cpf': '12345123455',
            'nome': 'gyhuer',
            'idade': '1',
            'altura': '1',
            'peso': '33',
            'sexo': 'F',
            'deficiencia': 'VISUAL'
        }

        new_tuple = Estudante.get_from_input(dic)

        inserir_estudante(conn=conn, cursor=cursor, student=new_tuple)

        cursor.close()
        conn.commit()

        print(f"Estudante {new_tuple.nome} cadastrado com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir estudante: {e}")

    finally:
        conn.close()