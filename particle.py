import random
import numpy as np

class Particle():
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random()*50, (-1)**(bool(random.getrandbits(1))) * random.random()*50])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])

    def __str__(self):
        print("Eu estou em ", self.position, " meu pbest é ", self.pbest_position)
    
    def move(self):
        self.position = self.position + self.velocity