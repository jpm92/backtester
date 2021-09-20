""" This file contains Machine Learning based strategies. Binary files
containing the models should be stored in an accessible path. """

from strategies.strategy import Strategy


class ThreeBarsNN(Strategy):
    def __init__(self, data, events, portfolio):
        self.data = data
        self.symbol_list = self.data.symbol_list
        self.events = events
        self.portfolio = portfolio
        self.name = 'Three Bars Neural Network'

        self.bought = self._calculate_initial_bought()

    def _calculate_initial_bought(self):
        bought = {}
        for symbol in self.symbol_list:
            bought[symbol] = False

        return bought

    def calculate_signals(self, event):
        pass
