import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(10000)
    rw.fill_walk()

    # Versão original
    # plt.scatter(rw.x_values, rw.y_values, s=5)
    # plt.show()
    
    # Versão com cmap
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.RdPu, edgecolors='none', s=5)
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break