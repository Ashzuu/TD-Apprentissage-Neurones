matrice_poids = [[0, -1, 1, 1],
                 [-1, 0, 1, -1],
                 [1, 1, 0, 1],
                 [1, -1, 1, 0]]

configs = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
           [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
           [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
           [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

f_activation = lambda x: 1 if x > 0 else 0

def syncPropagate(configs):
    """
    Propage le réseau de façon synchrone
    :param configs: Les configurations à utiliser
    :return: La nouvelle configuration du réseau
    """
    copyConfigs = configs.copy()
    nouvellesConfigs = []
    etats_stables = []
    cycles = []
    for i in range(len(configs)):
        config = copyConfigs[i]
        S_a = calculatePoids(matrice_poids[0], config)
        S_b = calculatePoids(matrice_poids[1], config)
        S_c = calculatePoids(matrice_poids[2], config)
        S_d = calculatePoids(matrice_poids[3], config)

        result = [S_a, S_b, S_c, S_d]

        display(i, result)
        if(result == config):
            print("------ ETATS STABLES DETECTES :) ------")
            etats_stables.append((i, result))

        nouvellesConfigs.append(result)

    return nouvellesConfigs


def asyncPropagate(configs):
    """
    Propage le réseau de façon asynchrone
    :param configs: Les configurations à utiliser
    :return: La nouvelle configuration du réseau
    """
    etats_stables = []
    nouvellesConfigs = configs.copy()
    for i in range(len(configs)):
        oldConfig = nouvellesConfigs[i].copy()
        for j in range(4):
            nouvellesConfigs[i][j] = calculatePoids(matrice_poids[j], nouvellesConfigs[i])

        display(i, nouvellesConfigs[i])
        if(oldConfig == nouvellesConfigs[i]):
            print("------ ETATS STABLES DETECTES :) ------")
            etats_stables.append((i, nouvellesConfigs[i]))


    return nouvellesConfigs


def calculatePoids(poids, config):
    """
    Calcule des poids selon la formule donnée pour avoir la valeur du neurone
    :param poids: Liste des poids
    :param config: Liste des configurations
    :return: La valeur de retour du neurone
    """
    somme = 0
    for i in range(len(poids)):
        somme += poids[i]*config[i]
    return f_activation(somme)

def display(i: int, value: list):
    """
    Affichage pratique et factorisé pour voir ce qu'il se passe dans les éléments
    :param i: Index du neurone à afficher
    :param value: Liste des valeurs à afficher
    :return: rien
    """
    print("---------- Pour n=", i, "----------")
    print("Somme de a : ", value[0])
    print("Somme de b : ", value[1])
    print("Somme de c : ", value[2])
    print("Somme de d : ", value[3])
    print(f"Soit ({value[0]}, {value[1]}, {value[2]}, {value[3]})")

syncPropagate(configs)
