import matplotlib.pyplot as plt
from random import random

f_activation = lambda x: 0 if x < 0 else 1
W_initial = [random(), random(), random()]

OU = [  ([0,0,1], 0),
        ([0,1,1], 1),
        ([1,0,1], 1),
        ([1,1,1], 1) ]

XOR = [  ([0,0,1], 0),
        ([0,1,1], 1),
        ([1,0,1], 1),
        ([1,1,1], 0) ]

ET = [  ([0,0,1], 0),
        ([0,1,1], 0),
        ([1,0,1], 0),
        ([1,1,1], 1) ]

def demarrer(exemples):
    W = W_initial.copy()
    eta = 0.2
    ne = 1
    NB_ITERATIONS = 20
    iterations = 0

    plt.figure()
    plt.xlim([0,1])
    plt.ylim([0,1])

    while ne != 0 and iterations < NB_ITERATIONS:
        ne = 0
        for index in range(len(exemples)):
            X,d = exemples[index]
            S = f_activation(W[0]*X[0] + W[1]*X[1] + W[2]*X[2])
            E = d - S
            if E != 0:
                ne += 1
                for i in range(len(W)):
                    W[i] += eta * E * X[i]
                a, b = -W[0] / W[1], -W[2] / W[1]
                y = [b, a * 1 + b]
                plt.plot([0, 1], y, color='gray', linestyle='--')
        iterations += 1
        print(ne)

    if ne > 0:
        print("L'opération ne converge pas.")

    a, b = -W[0] / W[1], -W[2] / W[1]
    plt.plot([0, 1], [b, a + b], color='blue')
    plt.show()

print("----- OU -----")
demarrer(OU)
print("----- ET -----")
demarrer(ET)
print("----- XOR -----")
demarrer(XOR)
