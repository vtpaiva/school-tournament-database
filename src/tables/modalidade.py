from dataclasses import dataclass
from common.utils import continuos_to_discrete

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
        
    def __str__(self):
        return (f"Modalidade(sport={self.sport}\nsex={self.sex}\nmin_age={self.min_age}\n"
                f"max_age={self.max_age}\nheight={self.height}\nweight={self.weight}\n"
                f"disability_type={self.disability_type}\nn_start={self.n_start}\n"
                f"n_reserve={self.n_reserve}\npont_rule={self.scor_rule})")
        
    @classmethod
    def get_from_input(cls):
        sport = input('Sport? ')
        sex = input('Sex? ')
        min_age = int(input('Minimum age? '))
        max_age = int(input('Maximum age? '))
        height = input('Height? ')
        weight = input('Weight? ')
        disability_type = input('Disability type? ')
        n_start = int(input('Stating team players? '))
        n_reserve = int(input('Reserve team players? '))
        scor_rule = input('Scoring rule? ')

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
    
    @classmethod
    def get_from_dict(cls, dicti):
        sport = dicti['sport']
        sex = dicti['sex']
        min_age = int(dicti['min_age'])
        max_age = int(dicti['max_age'])
        height = dicti['height']
        weight = dicti['weight']
        disability_type = dicti['disability']
        n_start = int(dicti['n_start'])
        n_reserve = int(dicti['n_reserve'])
        scor_rule = dicti['scor_rule']

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