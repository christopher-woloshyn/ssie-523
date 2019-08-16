import random as r

k = 1 # age-decay constant.
p = 0.1 # popularity threshold.

class Meme:
    id = 0 # global ID counter for all instantiated objects.
    def __init__(self):
        self.id = Meme.id
        Meme.id += 1

        self.age = 0
        self.popularity = r.random()
        self.alive = True
        self.children = []

    def getOlder(self):
        self.age += 1
        self.popularity = self.popularity ** (k*self.age)

    def reproduce(self):
        if r.random() < self.popularity and self.alive:
            child = Meme()
            self.children.append(child)
            return child

    def die(self):
        if self.popularity < p:
            self.alive = False
