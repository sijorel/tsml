__author__ = 'deschancesdjomo'

class blockClass:
    def __init__(self):
        self.name = None
        self.type = None
        self.state = []
        self.event = []
        self.transition = []
        self.observer = []


    def show(self):
        print(self.type + " " + self.name)
        print(" state: ")
        print(self.state)
        print(" event: ")
        print(self.event)
        print("end")


class transition:
    def __init__(self):
        self.event = None
        self.state1 = None
        self.state2 = None

class observer:
    pass