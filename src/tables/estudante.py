from dataclasses import dataclass
from common.utils import *

@dataclass
class Estudante:

    cpf: str
    nome: str
    idade: int
    altura: str
    peso: str
    sexo:str
    deficiencia: str

    @classmethod
    def get_from_input(cls):
        cpf = input("Digite o CPF do estudante (apenas números): ")

        if not valida_cpf(cpf):
            raise ValueError("CPF inválido. Deve ter 11 dígitos numéricos.")

        nome = input("Digite o nome do estudante: ")

        idade = input("Digite a idade do estudante: ")
        if not valida_idade(idade):
            raise ValueError("Idade inválida. Deve ser um número inteiro positivo.")

        altura = input("Digite a altura do estudante (em metros): ")
        if not valida_altura(altura):
            raise ValueError("Altura inválida. Deve ser um número entre 0.5 e 3.0 metros.")

        peso = input("Digite o peso do estudante (em kg): ")
        if not valida_peso(peso):
            raise ValueError("Peso inválido. Deve ser um número entre 10 e 300 kg.")

        sexo = input("Digite o sexo do estudante (M para masculino, F para feminino): ").upper()
        if sexo not in ["M", "F"]:
            raise ValueError("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")

        deficiencia = input("Digite a deficiência do estudante, se nenhuma digite NENHUMA: ")

        classificacao_altura = continuos_to_discrete(field=0, value=float(altura))
        classificacao_peso = continuos_to_discrete(field=1, value=float(peso))

        return cls(
            cpf, 
            nome,
            idade,
            classificacao_altura,
            classificacao_peso,
            sexo,
            deficiencia
        )
    
    @classmethod
    def get_from_dict(cls, dicti):
        cpf = dicti['cpf']

        if not valida_cpf(cpf):
            raise ValueError("CPF inválido. Deve ter 11 dígitos numéricos.")

        nome = dicti['nome']

        idade = dicti['idade']
        if not valida_idade(idade):
            raise ValueError("Idade inválida. Deve ser um número inteiro positivo.")

        altura = dicti['altura']
        if not valida_altura(altura):
            raise ValueError("Altura inválida.")

        peso = dicti['peso']
        if not valida_peso(peso):
            raise ValueError("Peso inválido.")

        sexo = dicti['sexo'].upper()
        if sexo not in ["M", "F"]:
            raise ValueError("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")

        deficiencia = dicti['deficiencia']

        classificacao_altura = continuos_to_discrete(field=0, value=float(altura))
        classificacao_peso = continuos_to_discrete(field=1, value=float(peso))

        return cls(
            cpf, 
            nome,
            idade,
            classificacao_altura,
            classificacao_peso,
            sexo,
            deficiencia
        )