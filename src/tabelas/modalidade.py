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
        esporte = input('Digite o esporte da modalidade: ')
        sexo = input(
            "Digite o sexo da modalidade (M para masculino, F para feminino): ").upper()
        idade_min = int(input('Digite a idade mínima: '))
        idade_max = int(input('Digite a idade máxima: '))
        altura = input('Digite a faixa de altura: ')
        peso = input('Digite a faixa de peso: ')
        deficiencia = input('Digite a deficiência da modalidade, se nenhuma digite NENHUMA: ')
        n_titulares = int(input('Digite o número de titulares: '))
        n_reservas = int(input('Digite o número de reservas: '))
        regra_pont = input('Digite a regra de pontuação: ')

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
