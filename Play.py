from Estado import Estado
import queue
from PodaAlphaBeta import PodaAlphaBeta
from Carta import Carta


def main():
    # aux = ["MAGICA", "AEREA", "TERRESTRE", "TROPA"]
    # print("write of 0,1,2 or 3")
    # answer = int(input())
    # typeCart = aux[answer] if answer == 1 or answer == 2 or answer == 3  or answer == 0 else main()
    # print("How many damage have your card?")
    # damageCard = int(input())
    # print("How many elixir have your card?")
    # elixir = int(input())

    # card_principal = Carta(name= "head", damage_base=damageCard, elixir=elixir, damage_card= answer+1)

    card_principal = Carta(name="head_proof", damage_base=750, elixir=6, damage_card=2)
    maso = card_principal.generateMaso()
    cardsForPlay = Carta.generateCardsToPlay()
    print("carta principal")
    print(card_principal.getName(),"--",card_principal.getElixir(),"--",card_principal.getDamageCard(),"--",card_principal.getDamageBase())
    print("cartas para jugar")
    for i in cardsForPlay:
        print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
    print("maso")
    for i in list(maso.queue):
        print(i.getName(), "--", i.getElixir(), "--", i.getDamageCard(), "--", i.getDamageBase())
    stateIntial = Estado(carta=card_principal, initial=True, cardsForPlay=cardsForPlay, maso=maso)
    #stateIntial.createNextStep()

    poda = PodaAlphaBeta()
    print(poda.alphaBetaDecision(stateIntial, 3))


if __name__ == '__main__':
    main()
