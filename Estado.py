import math
import random


class Estado:
    elixir = 0
    carta = 0
    value = 0
    alpha = -math.inf
    beta = math.inf
    initial = False
    terminal = False
    father = 0
    heuristic = 0
    daño = 0
    neighbors = []

    def __init__(self, carta="terrestre", father=0, initial=False, terminal=False, elixir=0, daño=0):
        self.father = father if not initial else None
        self.elixir = elixir
        self.setValueCart(carta)
        self.initial = initial
        self.daño = daño
        self.terminal = terminal
        self.heuristicEval()

    def heuristicEval(self):
        heuristicFather = self.father.getHeuristic() if not self.initial else 0
        self.heuristic = (heuristicFather + self.carta) * (self.daño - self.elixir)
        self.value = int(self.heuristic)

    def createNextStep(self):
        aux = ["MARINA", "AEREA", "TERRESTRE"]
        firt = Estado(carta=aux[random.randint(0, 2)], father=self, elixir=5, daño=random.randint(5, 20))
        second = Estado(carta=aux[random.randint(0, 2)], father=self, elixir=3, daño=random.randint(5, 20))
        thirt = Estado(carta=aux[random.randint(0, 2)], father=self, elixir=7, daño=random.randint(5, 20))
        fourth = Estado(carta=aux[random.randint(0, 2)], father=self, elixir=2, daño=random.randint(5, 20))
        fiveth = Estado(carta=aux[random.randint(0, 2)], father=self, elixir=1, daño=random.randint(5, 20))
        self.neighbors = [firt, second, thirt, fourth, fiveth]

    def actionResults(self):
        return self.neighbors

    """Getters"""

    def getHeuristic(self):
        return self.heuristic

    def getElixir(self):
        return self.elixir

    def getCarta(self):
        return self.carta

    def getValue(self):
        return self.value

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

    def isInitial(self):
        return self.initial
    def isTerminal(self):
        return self.terminal

    def getFather(self):
        return self.father
    def getDamage(self):
        return self.daño

    """setters"""

    def setValueCart(self, cart):
        if (str(cart).upper() == "TERRESTRE"):
            self.carta = 1;
        elif (str(cart).upper() == "AEREA"):
            self.carta = 2;
        elif (str(cart).upper() == "MARINA"):
            self.carta = 3;

    def setValue(self, value):
        self.value = value

    def setFather(self, father):
        self.father = father

    def setAlpha(self, alpha):
        self.alpha = alpha

    def setBeta(self, beta):
        self.beta = beta
