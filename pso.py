from space import Space
from particle import Particle

n_iterations = int(input("Informe o número de iterações: "))
target_error = float(input("Informe a taxa de erro aceitável: "))
n_particles = int(input("Informe o número de partículas: "))             

search_space = Space(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particles_vector
search_space.print_particles()
   
for iteration in range(0, n_iterations, 1):
    search_space.set_pbest()    
    search_space.set_gbest()

    if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break

    search_space.move_particles()

print("A melhor solução é: ", search_space.gbest_position, " em ", iteration + 1, " iterações.")