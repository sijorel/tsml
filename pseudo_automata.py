__author__ = 'deschancesdjomo'

class blockClass:
    def __init__(self):
        self.name = None
        self.type = None
        self.state = []
        self.classInstance = dict()
        self.event = []
        self.transition = []
        self.observer = []
        self.synchronisation = []

    def show(self):
        print(self.type + " " + self.name)
        if len(self.state) != 0:
            print(" state: ")
            print (self.state)
        print(" event: ")
        print(self.event)
        if len(self.transition) != 0:
            print(" transition: ")
            for trans in self.transition:
                print(trans.event + " : " + trans.state1 + " -> " + trans.state2)

        if len(self.synchronisation) != 0:
            print(" synchronization: ")
            for synchro in self.synchronisation:
                print(synchro.event + " : ")
                for evn in synchro.eventPathList:
                    print(evn.event + "."),
                    print(evn.values)
        print("end")


class transition:
    def __init__(self,event,state1, state2):
        self.event = event
        self.state1 = state1
        self.state2 = state2

class synchronisation:
    def __init__(self, event, eventPathList):
        self.event = event
        self.eventPathList = eventPathList

class eventpath:
    def __init__(self,event, values):
        self.event = event
        self.values = values

class observer:
    pass

