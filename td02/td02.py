matrice_poids = [[0, -1, 1, 1],
                 [-1, 0, 1, -1],
                 [1, 1, 0, 1],
                 [1, -1, 1, 0]]

configs = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
           [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
           [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
           [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

f_activation = lambda x: 1 if x > 0 else 0

def propagate(configs):
    copyConfigs = configs.copy()
    nouvellesConfigs = []
    for i in range(len(configs)):
        config = copyConfigs[i]
        x_a = calculatePoids(matrice_poids[0], config)
        x_b = calculatePoids(matrice_poids[1], config)
        x_c = calculatePoids(matrice_poids[2], config)
        x_d = calculatePoids(matrice_poids[3], config)
        print("---------- Pour n=", i, "----------")
        print(x_a)
        print(x_b)
        print(x_c)
        print(x_d)

        nouvellesConfigs.append([
            x_a, x_b, x_c, x_d
        ])

    return nouvellesConfigs



def calculatePoids(poids, config):
    somme = 0
    for i in range(len(poids)):
        somme += poids[i]*config[i]
    return f_activation(somme)

configs = propagate(configs)