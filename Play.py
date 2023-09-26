from Estado import Estado
from PodaAlphaBeta import PodaAlphaBeta
def main():
    aux = ["MARINA", "AEREA", "TERRESTRE"]
    print("write of 1, 2 or 3")
    answer = int(input())
    typeCart = aux[answer-1] if answer == 1 or answer == 2 or answer == 3 else main()

    stateIntial = Estado(carta = typeCart, initial = True)
    poda = PodaAlphaBeta()
    print(poda.alphaBetaDecision(stateIntial,5))
if __name__ == '__main__':
    main()