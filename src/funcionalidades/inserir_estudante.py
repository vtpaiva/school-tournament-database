from . import *
from ..tabelas.estudante import Estudante


def inserir_tupla(estudante, cursor):
    inserir_funcao(cursor, estudante.cpf)

    cursor.execute("""
        INSERT INTO Estudante (CPF, NOME, ALTURA, PESO, SEXO, IDADE, TIPO_DEFICIENCIA)
        VALUES (%(cpf)s, %(nome)s, %(altura)s, %(peso)s, %(sexo)s, %(idade)s, %(deficiencia)s)
    """, {'cpf': estudante.cpf,
          'nome': estudante.nome,
          'altura': estudante.altura,
          'peso': estudante.peso,
          'sexo': estudante.sexo,
          'idade': estudante.idade,
          'deficiencia': estudante.deficiencia})


def inserir_funcao(cursor, cpf):
    cursor.execute("""
        INSERT INTO Funcoes (CPF, FUNCAO)
        VALUES (%(cpf)s, 'E')
    """, {'cpf': cpf})


def inserir_estudante():
    try:
        conn, cursor = conectar_banco()

        nova_tupla = Estudante.get_from_input()

        inserir_tupla(estudante=nova_tupla, cursor=cursor)

        cursor.close()
        conn.commit()

        print(f"Estudante {nova_tupla.nome} cadastrado com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir estudante: {e}")

    finally:
        conn.close()
