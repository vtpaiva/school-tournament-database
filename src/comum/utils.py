import os
from numpy import inf
from dotenv import load_dotenv

from . import *

def conectar_banco():
    load_dotenv()

    conn_params = {
        'dbname': os.getenv("DBNAME"),
        'user': os.getenv("USERNAME"),
        'host': os.getenv("HOST"),
        'password': os.getenv("PASSWORD"),
        'port': os.getenv("PORT")
    }

    conn = connect(**conn_params)
    conn.autocommit = False

    return conn, conn.cursor()


def continuo_para_discreto(campo, valor=None):
    """
    Converte valores contínuos em categorias discretas dependendo do campo.

    Parameters:
        field (int | str): O campo que determina a categoria.
                           0 ou 'h' para altura e 1 ou 'w' para peso.
        value (float | None): O valor a ser convertido. Se for None, retorna 'QUALQUER'.

    Returns:
        str: A categoria correspondente ao valor fornecido.
    """

    if valor is None:
        return 'QUALQUER'

    faixas = {
        (0, 1.50): "MUITO BAIXO",
        (1.50, 1.60): "BAIXO",
        (1.60, 1.70): "MEDIO-BAIXO",
        (1.70, 1.80): "MEDIO",
        (1.80, 1.90): "ALTO",
        (1.90, inf): "MUITO ALTO"
    } if campo == 0 else {
        (0, 50): "MUITO LEVE",
        (50, 60): "LEVE",
        (60, 75): "MEDIO",
        (75, 90): "PESADO",
        (90, 110): "MUITO PESADO",
        (110, inf): "EXTREMAMENTE PESADO",
    }

    for intervalo, descricao in faixas.items():
        if intervalo[0] <= valor < intervalo[1]:
            return descricao

    return "QUALQUER"


def valida_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def valida_idade(idade):
    try:
        idade = int(idade)
        return idade > 0
    except ValueError:
        return False


def valida_altura(altura):
    try:
        altura = float(altura)
        return 1.0 <= altura <= 3.0
    except ValueError:
        return False


def valida_peso(peso):
    try:
        peso = float(peso)
        return 30 <= peso <= 200
    except ValueError:
        return False
