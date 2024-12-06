from . import *
from numpy import inf

def conectar_banco(
                    dbname='competicao',
                    user='postgres',
                    host='localhost',
                    password='password',
                    port=5432
                ):
    conn_params = {
        'dbname': dbname,
        'user': user,  
        'host': host,     
        'password': password,
        'port': port            
    }

    conn = connect(**conn_params)
    conn.autocommit = False

    return conn, conn.cursor()

def continuos_to_discrete(field, value=None):
    """
    Converte valores contínuos em categorias discretas dependendo do campo.
    
    Parameters:
        field (int | str): O campo que determina a categoria. 
                           0 ou 'h' para altura e 1 ou 'w' para peso.
        value (float | None): O valor a ser convertido. Se for None, retorna 'QUALQUER'.
        
    Returns:
        str: A categoria correspondente ao valor fornecido.
    """
    
    if value is None:
        return 'QUALQUER'
    
    faixas = {
        (0, 1.50): "MUITO BAIXO",
        (1.50, 1.60): "BAIXO",
        (1.60, 1.70): "MEDIO-BAIXO",
        (1.70, 1.80): "MEDIO",
        (1.80, 1.90): "ALTO",
        (1.90, inf): "MUITO ALTO"
    } if field == 0 else {
        (0, 50): "MUITO LEVE",
        (50, 60): "LEVE",
        (60, 75): "MEDIO",
        (75, 90): "PESADO",
        (90, 110): "MUITO PESADO",
        (110, inf): "EXTREMAMENTE PESADO",
    }

    for intervalo, descricao in faixas.items():
        if intervalo[0] <= value < intervalo[1]:
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
        return 0.5 <= altura <= 3.0  
    except ValueError:
        return False


def valida_peso(peso):
    try:
        peso = float(peso)
        return 10 <= peso <= 300  
    except ValueError:
        return False