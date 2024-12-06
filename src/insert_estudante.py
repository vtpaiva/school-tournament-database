from psycopg import connect
from tables.estudante import Estudante
from common.utils import conectar_banco

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

if __name__ == "__main__":
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

        inserir_estudante(conn, cursor, new_tuple)
        conn.commit()

        print(f"Estudante {new_tuple.nome} cadastrado com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir estudante: {e}")

    finally:
        cursor.close()
        conn.close()