class Rapper(object):
    likes = None
    def __init__(self, something):
        self.likes = something

    def talk(self): pass


class GoodRapper(Rapper):
    def talk(self):
        print("I like ", self.likes)

class EvilRapper(Rapper):
    def talk(self):
        print("I do not like ", self.likes)

sir_mix_alot = GoodRapper("big butts")
sir_mix_alittle = EvilRapper("big butts")

sir_mix_alot.talk()
sir_mix_alittle.talk()
