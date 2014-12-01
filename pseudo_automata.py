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
        else:
            print (self.classInstance)
        print(" event: ")
        print(self.event)

        if len(self.transition) != 0:
            print(" transition: ")
            for trans in self.transition:
                trans.show()
                #print(trans.event + " : " + trans.state1 + " -> " + trans.state2)
        if len(self.synchronisation) != 0:
            print(" synchronization: ")
            for synchro in self.synchronisation:
                synchro.show()
        print("end")


class transition:
    def __init__(self,event,state1, state2):
        self.event = event
        self.state1 = state1
        self.state2 = state2

    def show(self):
        print("\t" +self.event + " : " + self.state1 + " -> " + self.state2)


class synchronisation:
    def __init__(self, event, eventPathList):
        self.event = event
        self.eventPathList = eventPathList

    def show(self):
        print(self.event + " : ")
        for evn in self.eventPathList:
            evn.show()

class eventpath:
    def __init__(self,event, values):
        self.event = event
        self.values = values

    def show(self):
        print(self.event + ".")
        print(self.values)

class observer:
    pass

