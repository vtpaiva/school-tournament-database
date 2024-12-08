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
            "Digite o sexo da modalidade (M para masculino, F para feminino): ")
        idade_min = int(input('Digite a idade mínima: '))
        idade_max = int(input('Digite a idade máxima: '))

        if idade_min >= idade_max:
            raise ValueError("A idade mínima deve ser menor que a idade máxima.")

        altura = input('Digite a faixa de altura: (MUITO BAIXO, BAIXO, MEDIO-BAIXO, MEDIO, ALTO, MUITO ALTO, QUALQUER) ')
        peso = input('Digite a faixa de peso: (MUITO LEVE, LEVE, MEDIO, PESADO, MUITO PESADO, EXTREMAMENTE PESADO, QUALQUER) ')
        deficiencia = input('Digite a deficiência da modalidade: (VISUAL, MOTORA, INTELECTUAL, NENHUMA) ')
        n_titulares = int(input('Digite o número de titulares: '))
        n_reservas = int(input('Digite o número de reservas: '))
        regra_pont = input('Digite a regra de pontuação: (V%dE%dD%d) ')

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
