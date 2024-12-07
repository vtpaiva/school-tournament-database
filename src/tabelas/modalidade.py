from . import *


# Classe que representa uma modalidade esportiva
@dataclass
class Modalidade:
    
    esporte: str 
    sexo: str 
    idade_min: int  
    idade_max: int
    altura: str 
    peso: str  
    deficiencia: str 
    n_titulares: int  
    n_reservas: int 
    regra_pont: str 

    # Método de classe que cria uma instância de Modalidade com base na
    # entrada do usuário
    @classmethod
    def get_from_input(cls) -> object:
        esporte = input('Esporte: ')
        sexo = input('Sexo (M/F): ')
        idade_min = int(input('Idade mínima: '))
        idade_max = int(input('Idade máxima: '))
        altura = input('Faixa de altura: ')
        peso = input('Faixa de peso: ')
        deficiencia = input('Deficiência (ou NENHUMA): ')
        n_titulares = int(input('Número de titulares: '))
        n_reservas = int(input('Número de reservas: '))
        regra_pont = input('Regra de pontuação: ')

        return cls(
            esporte,
            sexo,
            idade_min,
            idade_max,
            altura,
            peso,
            deficiencia,
            n_titulares,
            n_reservas,
            regra_pont
        )
