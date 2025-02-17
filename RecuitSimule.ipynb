import random
import numpy as np
import matplotlib.pyplot as plt

# Points à visiter
points = [
    (565.0, 575.0), (25.0, 185.0), (345.0, 750.0), (945.0, 685.0), (845.0, 655.0),
    (880.0, 660.0), (25.0, 230.0), (525.0, 1000.0), (580.0, 1175.0), (650.0, 1130.0),
    (1605.0, 620.0), (1220.0, 580.0), (1465.0, 200.0), (1530.0, 5.0), (845.0, 680.0),
    (725.0, 370.0), (145.0, 665.0), (415.0, 635.0), (510.0, 875.0), (560.0, 365.0),
    (300.0, 465.0), (520.0, 585.0), (480.0, 415.0), (835.0, 625.0), (975.0, 580.0),
    (1215.0, 245.0), (1320.0, 315.0), (1250.0, 400.0), (660.0, 180.0), (410.0, 250.0),
    (420.0, 555.0), (575.0, 665.0), (1150.0, 1160.0), (700.0, 580.0), (685.0, 595.0),
    (685.0, 610.0), (770.0, 610.0), (795.0, 645.0), (720.0, 635.0), (760.0, 650.0),
    (475.0, 960.0), (95.0, 260.0), (875.0, 920.0), (700.0, 500.0), (555.0, 815.0),
    (830.0, 485.0), (1170.0, 65.0), (830.0, 610.0), (605.0, 625.0), (595.0, 360.0),
    (1340.0, 725.0), (1740.0, 245.0)
]

# Fonction de calcul de la distance euclidienne
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Fonction de calcul de la distance totale pour un chemin donné
def total_distance(path):
    distance = 0.0
    for i in range(len(path) - 1):
        distance += euclidean_distance(points[path[i]], points[path[i + 1]])
    distance += euclidean_distance(points[path[-1]], points[path[0]])  # Retour au point de départ
    return distance

# Perturber une solution en échangeant deux points aléatoires
def perturb_solution(path):
    new_path = path[:]
    i, j = random.sample(range(len(path)), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

# Méthode de recuit simulé
def simulated_annealing(initial_path, initial_temperature, cooling_rate, min_temperature):
    current_path = initial_path
    current_distance = total_distance(current_path)
    temperature = initial_temperature
    best_path = current_path
    best_distance = current_distance

    while temperature > min_temperature:
        new_path = perturb_solution(current_path)
        new_distance = total_distance(new_path)
        delta_distance = new_distance - current_distance

        if delta_distance < 0 or random.random() < np.exp(-delta_distance / temperature):
            current_path = new_path
            current_distance = new_distance

            if current_distance < best_distance:
                best_path = current_path
                best_distance = current_distance

        temperature *= cooling_rate
        print(f'Temperature: {temperature:.2f}, Best distance: {best_distance:.2f}')

    return best_path

# Fonction de visualisation du chemin
def plot_path(path):
    path_points = [points[i] for i in path] + [points[path[0]]]
    x, y = zip(*path_points)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title('Optimized Path')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Paramètres du recuit simulé
initial_temperature = 10000
cooling_rate = 0.999
min_temperature = 0.1

# Chemin initial aléatoire
initial_path = list(range(len(points)))
random.shuffle(initial_path)

# Exécuter le recuit simulé et afficher le chemin
best_path = simulated_annealing(initial_path, initial_temperature, cooling_rate, min_temperature)
print(f'Best path: {best_path}')
print(f'Total distance: {total_distance(best_path)}')
plot_path(best_path)
