import math
import random
import queue
from copy import copy
from copy import deepcopy

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
    def doCopy(self, maso):
        aux = queue.Queue()
        for  i in list(maso.queue):
            aux.put(i)
        return aux


    def createNextStep(self, state):
        if(not state.isInitial()):
            card = deepcopy(state.getCarta())
            setPlay = deepcopy(state.getCardsForPlay())
            maso = state.doCopy(state.getMaso())
            print("maso")
            for i in list(maso.queue):
                print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
            print("cartas par jugar")
            for i in setPlay:
                print(i.getName(),"--",i.getElixir(),"--",i.getDamageCard(),"--",i.getDamageBase())
            print("carta jugada")
            print(card.getName(),"--",card.getElixir(),"--",card.getDamageCard(),"--",card.getDamageBase())

            for i in setPlay:
                if card.getDamageCard() == i.getDamageCard() and card.getName() == i.getName() and card.getElixir() == i.getElixir() and card.getDamageBase() == i.getDamageBase():
                    setPlay.remove(i)
            if (len(setPlay) == 4):
                setPlay.append(maso.get())
                maso.put(card)
                state.setCartasForPlay(setPlay)
                state.setMaso(maso)
                print ("actualizacion")
                print("maso")
                for i in list(maso.queue):
                    print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
                print("cartas para jugar")
                for i in setPlay:
                    print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())

            else:
                raise ValueError("no entro a la lista de vecinos")

    def generateStates(self):
        self.neighbors_states = []
        for i in self.cardsForPlay:
            estado_aux = Estado(carta=i, father=self, cardsForPlay=copy(self.cardsForPlay), maso=self.doCopy(self.maso))
            estado_aux.createNextStep(estado_aux)
            self.neighbors_states.append(estado_aux)


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
    def setCartasForPlay(self,lista_1):
        self.cardsForPlay = lista_1

    def setMaso(self, maso_1):
        self.maso = maso_1


