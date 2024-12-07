from . import *
from ..comum.utils import *


# Classe que representa um estudante no banco
@dataclass
class Estudante:
    cpf: str  
    nome: str  
    idade: int  
    altura: str 
    peso: str  
    sexo: str  
    deficiencia: str

    # Método de classe que cria uma instância de Estudante a partir de
    # entradas do usuário
    @classmethod
    def get_from_input(cls):
        cpf = input("Digite o CPF do estudante (apenas números): ")
        if not valida_cpf(cpf):
            raise ValueError("CPF inválido. Deve ter 11 dígitos numéricos.")

        nome = input("Digite o nome do estudante: ")
        idade = input("Digite a idade do estudante: ")

        altura = input("Digite a altura do estudante (em metros): ")
        if not valida_altura(altura=altura):
            raise ValueError(
                "Valor de altura inválido. (O valor deve estar entre 1 e 3 metros)")

        peso = input("Digite o peso do estudante (em kg): ")
        if not valida_peso(peso=peso):
            raise ValueError(
                "Valor de peso inválido. (O valor deve estar entre 20 e 200 kilos)")

        sexo = input(
            "Digite o sexo do estudante (M para masculino, F para feminino): ").upper()

        deficiencia = input(
            "Digite a deficiência do estudante, se nenhuma digite NENHUMA: ")

        classificacao_altura = continuo_para_discreto(
            campo=ALTURA, valor=float(altura))

        classificacao_peso = continuo_para_discreto(
            campo=PESO, valor=float(peso))

        return cls(
            cpf,
            nome,
            idade,
            classificacao_altura,
            classificacao_peso,
            sexo,
            deficiencia
        )
