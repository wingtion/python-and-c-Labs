from abc import ABC, abstractmethod


class FreqCounter(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FreqCounter):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            data = file.read()
        letters = list(data)
        freqs = [(letter, letters.count(letter)) for letter in set(letters)]
        print(freqs)


class DictCount(FreqCounter):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            data = file.read()
        freqs = {letter: data.count(letter) for letter in set(data)}
        print(freqs)


list_counter = ListCount('weirdWords.txt')
list_counter.calculateFreqs()

dict_counter = DictCount('weirdWords.txt')
dict_counter.calculateFreqs()