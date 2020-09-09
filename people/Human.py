from random import random
from math import ceil


class Human:

    def __init__(self, name='Vasya'):
        self.name = name
        self.satiety = ceil(random() * 100)
        self.money = ceil(random() * 100)
        self.happiness = ceil(random() * 100)

    def say(self):
        print(self.name + ' say: Я МУЖИК!')

    def work(self):
        self.satiety -= ceil(random() * 100)
        self.money += ceil(random() * 100)
        self.happiness -= ceil(random() * 100)
        print(self.satiety, self.money, self.happiness)

    def eat(self):
        self.satiety += ceil(random() * 100)
        self.money -= ceil(random() * 100)
        self.happiness += ceil(random() * 100)
        print(self.satiety, self.money, self.happiness)

    def fishing(self):
        self.satiety -= ceil(random() * 100)
        self.happiness += ceil(random() * 100)
        print(self.satiety, self.money, self.happiness)