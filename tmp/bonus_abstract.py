from abc import abstractmethod


class Bonus:
    @abstractmethod
    def process(self, player):
        pass
