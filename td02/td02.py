import random
import itertools

poids1 =   [[0, -1, 1, 1],
           [-1, 0, 1, -1],
           [1, 1, 0, 1],
           [1, -1, 1, 0]]

configs1 = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
           [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
           [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
           [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

f_activation = lambda x: 1 if x > 0 else 0

def syncPropagate(configs, matrice_poids):
    """
    Propage le réseau de façon synchrone
    :param configs: Les configurations à utiliser
    :return: La nouvelle configuration du réseau
    """
    print("Pour la config :", configs)
    print("Pour la matrice de poids :", matrice_poids)
    copyConfigs = configs.copy()
    nouvellesConfigs = []
    etats_stables = []
    cycles = []
    for i in range(len(configs)):
        isEtatStable = False
        config = copyConfigs[i]
        result = []
        for j in range(len(config)):
            result.append(calculatePoids(matrice_poids[j], config))


        checkCycles = []
        for l in range(len(result)):
            checkCycles.append(calculatePoids(matrice_poids[l], result))

        display(i, result)

        if (result == config):
            print("------ ETATS STABLES DETECTES :) ------")
            isEtatStable = True
            etats_stables.append((i, result))

        if checkCycles == config and not isEtatStable:
            print("------ CYCLES DETECTES :) ------")
            cycles.append([config, result])


        nouvellesConfigs.append(result)

    return {
            "configs":nouvellesConfigs,
            "etats_stables":etats_stables,
            "cycles":cycles
        }


def asyncPropagate(configs, matrice_poids):
    """
    Propage le réseau de façon asynchrone
    :param configs: Les configurations à utiliser
    :return: La nouvelle configuration du réseau
    """
    etats_stables = []
    cycles = []
    isEtatStable = False
    nouvellesConfigs = configs.copy()
    for i in range(len(configs)):
        oldConfig = nouvellesConfigs[i].copy()
        for j in range(len(matrice_poids)):
            nouvellesConfigs[i][j] = calculatePoids(matrice_poids[j], nouvellesConfigs[i])

        display(i, nouvellesConfigs[i])
        if(oldConfig == nouvellesConfigs[i]):
            print("------ ETATS STABLES DETECTES :) ------")
            etats_stables.append((i, nouvellesConfigs[i]))
            isEtatStable = True

        detectCycles = []
        for j in range(len(matrice_poids)):
            detectCycles.append(calculatePoids(matrice_poids[j], nouvellesConfigs[i]))

        if(detectCycles == oldConfig and not isEtatStable):
            print("------ CYCLES DETECTES :) ------")
            cycles.append([nouvellesConfigs[i], detectCycles])



    return {
        "configs" : nouvellesConfigs,
        "etats_stables" : etats_stables,
        "cycles" : cycles
    }


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

def generer_poids(n=10):
    poids = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            val = random.choice([-1, 1])
            poids[i][j] = val
            poids[j][i] = val

    return poids

def generer_configs(n=10):
    return [list(c) for c in itertools.product([0, 1], repeat=n)]

# A activer pour tester unitairement avec la configuration initiale, mettre 'False' pour désactiver ce bloc
if False:
    syncPropagate(configs1, poids1)
    asyncPropagate(configs1, poids1)


# A activer pour l'analyse statistiques, mettre 'False' pour désactiver ce bloc
if True:
    statsSync = []
    statsAsync = []

    NOMBRE_LANCEE = 10

    for i in range(NOMBRE_LANCEE):
        configs = generer_configs(10)
        poids = generer_poids(10)

        resultSync = syncPropagate(configs, poids)
        statsSync.append((len(resultSync["etats_stables"]),len(resultSync["cycles"])))

        resultAsync = asyncPropagate(configs, poids)
        statsAsync.append((len(resultAsync["etats_stables"]),len(resultAsync["cycles"])))

    print(statsSync)
    print(statsAsync)

    sommeStatsStablesSync = 0
    sommeCyclesSync = 0

    sommeStatsStablesAsync = 0
    sommeCyclesAsync = 0

    for i in range(NOMBRE_LANCEE):
        sommeStatsStablesSync += statsSync[i][0]
        sommeCyclesSync += statsSync[i][1]

        sommeStatsStablesAsync += statsAsync[i][0]
        sommeCyclesAsync += statsAsync[i][1]

    print("Pour la propagation synchrone : ", sommeStatsStablesSync, "états stables, et", sommeCyclesSync, "cycles")
    print("Pour la propagation asynchrone :", sommeStatsStablesAsync, "états stables, et", sommeCyclesAsync, "cycles")
