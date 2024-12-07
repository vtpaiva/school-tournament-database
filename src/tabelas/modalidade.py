from . import *


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

    @classmethod
    def get_from_input(cls):
        esporte = input('Digite o esporte da modalidade: ')
        sexo = input(
            'Digite o sexoo ao qual a modalidade é destinada (M para masculino, F para feminino): ')
        idade_min = int(input('Digite a idade mínima da modalidade: '))
        idade_max = int(input('Digite a idade máxima da modalidade: '))
        altura = input('Digite a faixa de altura da modalidade: ')
        peso = input('Digite a faixa de peso da modalidade: ')
        deficiencia = input(
            'Digite o tipo de deficiência da modalidade, se nenhuma digite NENHUMA: : ')
        n_titulares = int(
            input('Digite o número de jogadores titulares por partida da modalidade: '))
        n_reservas = int(
            input('Digite o número de jogadores reservas por partida da modalidade: '))
        regra_pont = input('Digite a regra de pontuação da modalidade: ')

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