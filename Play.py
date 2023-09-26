from Estado import Estado
from PodaAlphaBeta import PodaAlphaBeta
def main():
    aux = ["MAGICA", "AEREA", "TERRESTRE", "TROPA"]
    print("write of 0,1, 2 or 3")
    answer = int(input())
    typeCart = aux[answer] if answer == 1 or answer == 2 or answer == 3  or answer == 0 else main()

    stateIntial = Estado(carta = typeCart, initial = True)
    poda = PodaAlphaBeta()
    print(poda.alphaBetaDecision(stateIntial,5))
if __name__ == '__main__':
    main()