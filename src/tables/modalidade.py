from . import *

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
        sport = input('Digite o esporte da modalidade: ')
        sex = input('Digite o sexo ao qual a modalidade é destinada (M para masculino, F para feminino): ')
        min_age = int(input('Digite a idade mínima da modalidade: '))
        max_age = int(input('Digite a idade máxima da modalidade: '))
        height = input('Digite a faixa de altura da modalidade: ')
        weight = input('Digite a faixa de peso da modalidade: ')
        disability_type = input('Digite o tipo de deficiência da modalidade, se nenhuma digite NENHUMA: : ')
        n_start = int(input('Digite o número de jogadores titulares por partida da modalidade: '))
        n_reserve = int(input('Digite o número de jogadores reservas por partida da modalidade: '))
        scor_rule = input('Digite a regra de pontuação da modalidade: ')

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