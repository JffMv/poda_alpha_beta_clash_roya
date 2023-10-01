import math
import random
import queue
from copy import copy

from Carta import Carta


class Estado:
    elixir = 0
    value = 0
    alpha = -math.inf
    beta = math.inf
    initial = False
    terminal = False
    father = 0
    heuristic = 0
    daño = 0
    cardsForPlay = []
    maso = queue.Queue()
    neighbors_states = []

    def __init__(self, carta, father=0, initial=False, terminal=False, cardsForPlay=[], maso=queue.Queue()):
        self.carta = carta
        self.father = father if not initial else None
        self.elixir = carta.getElixir()
        self.initial = initial
        self.daño = carta.getDamageBase()
        self.terminal = terminal
        self.heuristicEval()
        self.cardsForPlay = cardsForPlay
        self.maso = maso

    def heuristicEval(self):
        heuristicFather = self.father.getHeuristic() if not self.initial else 0
        self.heuristic = heuristicFather + abs((self.carta.getDamageCard() - self.elixir) * self.daño)
        self.value = int(self.heuristic)

    "la lista de neighbors debe llegar 4 elementos"

    def createNextStep(self, state):

        card = copy(state.getCarta())
        setPlay = copy(state.getCardsForPlay())
        maso = copy(state.getMaso())
        print("maso")
        for i in list(maso.queue):
            print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
        print("cartas par jugar")
        for i in state.getCardsForPlay():
            print(i.getName(),"--",i.getElixir(),"--",i.getDamageCard(),"--",i.getDamageBase())
        print("carta jugada")
        print(card.getName(),"--",card.getElixir(),"--",card.getDamageCard(),"--",card.getDamageBase())

        for i in setPlay:
            if card.getDamageCard() == i.getDamageCard() and card.getName() == i.getName() and card.getElixir() == i.getElixir() and card.getDamageBase() == i.getDamageBase():
                setPlay.remove(i)

        if (len(setPlay) == 4):
            setPlay.append(maso.get())
            maso.put(card)
            state.generateStates(state, setPlay, maso)
            print ("actualizacion")
            print("maso")
            for i in list(maso.queue):
                print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
            print("cartas par jugar")
            for i in state.getCardsForPlay():
                print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())

        else:
            raise ValueError("no entro a la lista de vecinos")

    def generateStates(self, state=None, setPlay=None, maso=None):
        if (state != None or setPlay != None or maso != None):
            listNeigbors = []
            for i in setPlay:
                listNeigbors.append(Estado(carta=i, father=state, cardsForPlay=setPlay, maso=maso,initial=False))
            state.setNeighborsState(listNeigbors)
        else:
            self.neighbors_states = []
            for i in self.cardsForPlay:
                self.neighbors_states.append(
                    Estado(carta=i, father=self, cardsForPlay=self.cardsForPlay, maso=self.maso))

    def actionResults(self):
        return self.neighbors_states

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

    def getMaso(self):
        return self.maso

    def getCardsForPlay(self):
        return self.cardsForPlay

    """setters"""

    def setValue(self, value):
        self.value = value

    def setFather(self, father):
        self.father = father

    def setAlpha(self, alpha):
        self.alpha = alpha

    def setBeta(self, beta):
        self.beta = beta

    def setNeighborsState(self, listNeighbors):
        self.neighbors_states = listNeighbors


