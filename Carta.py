import queue
import random


class Carta:
    def __init__(self, name, damage_base, elixir, damage_card):
        self.name = name
        self.damage_base = damage_base
        self.elixir = elixir
        self.damage_card = damage_card

    @classmethod
    def generateCardsToPlay(cls):
        """son las cartas con las que se juega"""

        playOfCards = []
        for i in range(5):
            var = Carta(name=i, damage_base=random.randint(750, 1800),
                        elixir=random.randint(1, 9),
                        damage_card=random.randint(0, 3))
            playOfCards.append(var)
        return playOfCards

    def generateMaso(self):
        """Son todas las cartas guardadas para jugar"""
        maso = queue.Queue()
        for i in range(7):
            var = Carta(name=i, damage_base=random.randint(750, 1800),
                        elixir=random.randint(1, 9),
                        damage_card=random.randint(0, 3))
            maso.put(var)
        maso.put(self)
        return maso

    """getters"""

    def getName(self):
        return self.name

    def getDamageBase(self):
        return self.damage_base

    def getElixir(self):
        return self.elixir

    def getDamageCard(self):
        return self.damage_card

    def getElement(self):
        aux = ["MAGICA", "AEREA", "TERRESTRE", "TROPA"]
        return aux[self.damage_card]
