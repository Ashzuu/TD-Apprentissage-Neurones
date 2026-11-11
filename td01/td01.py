from random import random

f_activation = lambda x:0 if x < 0 else 1

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

def makeGraph(W: list):
    from matplotlib.pylab import plot, xlim, ylim, show, title
    xlim([-0.5, 1.5])
    ylim([-0.5, 1.5])
    title("TD01")
    a=-W[0]/W[1]
    b=-W[2]/W[1]
    y = [b, a * 1 + b]
    plot([0, 1], y)
    show()

def demarrer(exemples: list):
    W = [random(), random(), random()]
    eta = 0.2
    ne = 1
    NB_ITERATIONS = 20
    iterations = 0
    while ne != 0 and iterations < NB_ITERATIONS:
        ne = 0
        for index in range(len(exemples)):
            X, d = exemples[index]
            S = f_activation(W[0]*X[0] + W[1]*X[1] + W[2]*X[2])
            E = d-S
            if E != 0:
                ne += 1
                for i in range(len(W)):
                    W[i] += eta*E*X[i]
        iterations += 1
        print(ne)
    if ne > 0:
        print("L'opération ne converge pas.")

    makeGraph(W)

print("----- OU -----")
demarrer(OU)
print("----- ET -----")
demarrer(ET)
print("----- XOR -----")
demarrer(XOR)



