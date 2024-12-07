import os
from numpy import inf
from dotenv import load_dotenv

from . import *


# Constantes do ambiente
ALTURA, PESO = 0, 1


# Função para conectar ao banco de dados utilizando variáveis de ambiente
def conectar_banco() -> tuple:
    """
    Estabelece a conexão com o banco de dados utilizando variáveis de ambiente.

    As variáveis de conexão são carregadas de um arquivo .env usando o 'dotenv'.
    A conexão é configurada com 'autocommit = False'.

    Returns:
        conn (object): Conexão com o banco de dados.
        cursor (object): Cursor para executar comandos SQL.
    """

    load_dotenv()

    # Define os parâmetros de conexão com o banco a partir das variáveis de
    # ambiente
    conn_params = {
        'dbname': os.getenv("DBNAME"),
        'user': os.getenv("USERNAME"),
        'host': os.getenv("HOST"),
        'password': os.getenv("PASSWORD"),
        'port': os.getenv("PORT")
    }

    conn = connect(**conn_params)
    conn.autocommit = False  # Desativa o autocommit para controle manual de transações

    return conn, conn.cursor()


# Função que converte valores contínuos (altura ou peso) em categorias
# discretas
def continuo_para_discreto(campo: int, valor: float =None) -> str:
    """
    Converte valores contínuos (altura ou peso) em categorias discretas.

    Parâmetros:
        campo (int | str): Identifica o campo que será categorizado.
                           0 ou 'h' para altura, 1 ou 'w' para peso.
        valor (float | None): O valor contínuo a ser categorizado.
                              Se for None, retorna 'QUALQUER'.

    Retorno:
        str: Categoria discreta correspondente ao valor fornecido.
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
    } if campo == ALTURA else {
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

    # Retorna 'QUALQUER' se o valor não se enquadrar em nenhuma faixa
    return "QUALQUER"


# Função para validar se o CPF é válido
def valida_cpf(cpf: str) -> bool:
    """
    Verifica se o CPF contém apenas números e se possui exatamente 11 dígitos.

    Parâmetros:
        cpf (str): CPF fornecido pelo usuário.

    Retorno:
        bool: True se o CPF for válido, False caso contrário.
    """

    return cpf.isdigit() and len(cpf) == 11


# Função para validar se a altura está no intervalo permitido (1m a 3m)
def valida_altura(altura: float) -> bool:
    """
    Valida se a altura está dentro do intervalo permitido (1.0 a 3.0 metros).

    Parâmetros:
        altura (str): Altura fornecida pelo usuário.

    Retorno:
        bool: True se a altura for válida, False caso contrário.
    """

    try:
        altura = float(altura)
        return 1.0 <= altura <= 3.0 
    except ValueError:
        return False


# Função para validar se o peso está no intervalo permitido (30kg a 200kg)
def valida_peso(peso: float) -> bool:
    """
    Valida se o peso está dentro do intervalo permitido (30kg a 200kg).

    Parâmetros:
        peso (str): Peso fornecido pelo usuário.

    Retorno:
        bool: True se o peso for válido, False caso contrário.
    """
    
    try:
        peso = float(peso)
        return 30 <= peso <= 200  
    except ValueError:
        return False  
