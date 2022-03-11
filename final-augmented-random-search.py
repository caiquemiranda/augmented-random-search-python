# importação das bibliotecas
import os
import numpy as np

# configuração dos hiperparametros
class Hp():
    def __init__(self):
        self.nb_steps = 1000 # numero de episódios
        self.episode_lenght = 1000 # máxima duração dos episódios
        self.learning_rate = 0.02 # taxa de aprendizado
        self.nb_directions = 16 # numero de direções, matrizes de perturbações contruidas
        self.nb_best_directions = 16 # mellhores recompensas
        assert self.nb_best_directions <= self.nb_directions # garantir que o best directions é menor que o directions
        self.noise = 0.03 # ruido, filtro de variancia nos dados
        self.seed = 1 # manter os resultados
        self.env_name = ''