from dataclasses import dataclass
from utils.utils import continuos_to_discrete

@dataclass
class Modalidade:

    sport: str
    sex: str
    min_age: int
    max_age: int
    height: str
    weight: str
    disability_type: str
    n_start: int
    n_reserve: int
    scor_rule: str

    def __post_init__(self):
        if self.min_age < 0 or self.max_age < 0:
            raise ValueError("Ages cannot be less than 1.")
        if self.min_age >= self.max_age:
            raise ValueError("Idade mínima não pode ser maior ou igual à idade máxima.")

        if self.n_start <= 0 or self.n_reserve < 0:
            raise ValueError("Número de jogadores não pode ser negativo.")
        
        if not self.sport:
            raise ValueError("O esporte não pode ser vazio.")
        
    def __str__(self):
        return (f"Modalidade(sport={self.sport}\nsex={self.sex}\nmin_age={self.min_age}\n"
                f"max_age={self.max_age}\nheight={self.height}\nweight={self.weight}\n"
                f"disability_type={self.disability_type}\nn_start={self.n_start}\n"
                f"n_reserve={self.n_reserve}\npont_rule={self.scor_rule})")
        
    @classmethod
    def get_from_input(cls):

        sport = input('Sport?')
        sex = input('Sex?')
        min_age = int(input('Minimum age?'))
        max_age = int(input('Maximum age?'))
        height = float(input('Height?'))
        weight = float(input('Weight?'))

        if height <= 0 or weight <= 0:
            raise ValueError("Altura ou peso não podem ser menores que zero.")
        
        height = continuos_to_discrete(field=0, value=height)
        weight = continuos_to_discrete(field=1, value=weight)
        disability_type = input('Disability type?')
        n_start = int(input('Stating team players?'))
        n_reserve = int(input('Reserve team players?'))
        scor_rule = input('Scoring rule?')

        return cls(
                    sport, 
                    sex, 
                    min_age, 
                    max_age, 
                    height, 
                    weight, 
                    disability_type, 
                    n_start, 
                    n_reserve, 
                    scor_rule
                )