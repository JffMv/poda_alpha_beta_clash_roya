import math
from Estado import Estado


class PodaAlphaBeta:
    list_states = []
    state = 0
    number = 0

    def __init__(self):

        pass

    def minValue(self, TState, number_d, number_alpha, number_beta):
        print(number_d, " mirameeeeeeee ___________________________")
        if (number_d == 0 or TState.isTerminal()):
            print("paseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" , number_d)
            return TState.getHeuristic()

        else:
            print(number_d, " mirameeeeeeee ___________________________")
            # TState.setValue(math.inf)
            # if (number_d != self.state ):

            TState.generateStates()  # unique for this case

            value = math.inf
            nextStates = TState.actionResults()
            for i in range(len(nextStates)):
                state = nextStates[i]
                number = self.maxValue(state, number_d - 1, number_alpha, number_beta)
                value = min(value, number)
                number_beta = min(value, number_beta)
                # print (self.state ," uno ", number_d)
                if (number_beta <= number_alpha):
                    break
            return value

    def maxValue(self, TState, number_d, number_alpha, number_beta):
        print(number_d, " mirameeeeeeee _ mazx___________________________")
        if (number_d == 0 or TState.isTerminal()):

            print("paseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return TState.getHeuristic()

        else:
            print(number_d, " mirameeeeeeee _ mazx___________________________")

            TState.generateStates()  # unique for this case
            value = -math.inf
            nextStates = TState.actionResults()
            for i in range(len(nextStates)):
                state = nextStates[i]
                number = self.minValue(state, number_d - 1, number_alpha, number_beta)
                value = max(value, number)
                number_alpha = max(value, number_alpha)
                if (self.state == number_d):
                    self.list_states.append([state, value])
                    self.number += 1

                if (number_alpha >= number_beta):
                    break
            return value

    def alphaBetaDecision(self, TState, number_d):
        real_answer = "no hay camino"
        self.state = number_d
        value = self.maxValue(TState, number_d, -math.inf, math.inf)
        posibles_answers = TState.actionResults()
        results = []
        for i in posibles_answers:
            carta2 = i.getCarta()
            print("Name of Card: ", carta2.getName(), "whith damabe base: ", carta2.getDamageBase(),"whith damabe of card: ", carta2.getDamageCard(),"whith elixir: ", carta2.getElixir())

        for state in self.list_states:
            print(state[1], "guaradado")
            if(state[1] == value):
                carta =state[0].getCarta()
                real_answer = "Name of Card: ", carta.getName(), "whith damabe base: ", carta.getDamageBase(),"whith damabe of card: ", carta.getDamageCard(),"whith elixir: ", carta.getElixir()," whith damage in state: ", state[0].getDamage()
                break

        print(value, "value")
        print(self.number , "Times into to save states")
        print(len(self.list_states), "Number the states save in the add implementation of code")
        return real_answer
