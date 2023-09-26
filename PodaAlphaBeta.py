import math
from Estado import Estado
class PodaAlphaBeta:
    list_states = []
    state = 0
    def __init__(self):

        pass
    def minValue(self, TState, number_d, number_alpha, number_beta):
        if (number_d == 0 or TState.isTerminal()):

            return TState.getHeuristic()

        #TState.setValue(math.inf)
        TState.createNextStep() # unique for this case
        value = math.inf


        for state in TState.actionResults():

            number = self.maxValue(state, number_d - 1, number_alpha, number_beta)
            value = min(value, number)
            number_beta = min(value, number_beta)
            #print (self.state ," uno ", number_d)
            if (number_beta <= number_alpha):
                break
        return value



    def maxValue(self, TState, number_d, number_alpha, number_beta):
        if (number_d == 0 or TState.isTerminal()): return TState.getHeuristic()

        #TState.setValue(-math.inf)
        TState.createNextStep()  # unique for this case
        value = -math.inf

        for state in TState.actionResults():
            if (self.state - 1 == number_d-1): self.list_states.append([state, value])
            number = self.minValue(state, number_d - 1, number_alpha, number_beta)
            value = max(value, number)
            number_alpha = max(value, number_alpha)

            if (number_alpha >= number_beta): break

        return value



    def alphaBetaDecision(self, TState, number_d):
        real_answer ="no hay camino"
        self.state = number_d
        value = self.maxValue(TState, number_d, -math.inf, math.inf)
        posibles_answers = TState.actionResults()
        for i in posibles_answers:
            print(i.getCarta(), "carta")
            print(i.getDamage(), "daño")

        for state in self.list_states:
            #print(state[0].getCarta(), "carta guardada")
            #print(state[0].getDamage(), "daño guardado")

            real_answer = (state[0].getCarta(), " whith damage: ", state[0].getDamage()) if state[1]== value else real_answer
        print(len(self.list_states))
        return real_answer

