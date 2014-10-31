__author__ = 'deschancesdjomo'

class Node(object):
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

class Model(Node):
    def __init__(self,block, classlist):
        self.type = "model"
        self.block = block
        self.classlist = classlist

    def children(self):
        nodelist = []
        if self.block is not None : nodelist.append(("block", self.block))

        for i, child in enumerate(self.classlist or []):
            nodelist.append(("classlist[%d]" % i, child))
        return tuple(nodelist)

    attr_names=()

class BlockDecl(Node):
    def __init__(self, type, name, body):
        self.type = type
        self.name = name
        self.body = body

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        if self.type is not None: nodelist.append(("type", self.type))
        if self.body is not None: nodelist.append(("blockbody", self.body))
        return tuple(nodelist)

    attr_names = ()

class BasicBlockBody(Node):
    def __init__(self, stateclause, eventclause, transitionclause, observerclause):
        self.stateclause = stateclause
        self.eventclause = eventclause
        self.transitionclause = transitionclause
        self.observerclause = observerclause

    def children(self):
        nodelist = []
        if self.stateclause is not None: nodelist.append(("stateclause", self.stateclause))
        if self.eventclause is not None: nodelist.append(("eventclause", self.eventclause))
        if self.transitionclause is not None: nodelist.append(("transitionclause", self.transitionclause))
        if self.observerclause is not None: nodelist.append(("observerclause", self.observerclause))
        return tuple(nodelist)

    attr_names = ()


class InternalBlockBody(Node):
    def __init__(self, composedblockclause, eventclause, synchronizationclause, observerclause):
        self.composedblockclause = composedblockclause
        self.eventclause = eventclause
        self.synchronizationclause = synchronizationclause
        self.observerclause = observerclause

    def children(self):
        nodelist = []
        if self.composedblockclause is not None: nodelist.append(("composedblockclause", self.composedblockclause))
        if self.eventclause is not None: nodelist.append(("eventclause", self.eventclause))
        if self.synchronizationclause is not None: nodelist.append(("synchronizationclause", self.synchronizationclause))
        if self.observerclause is not None: nodelist.append(("observerclause", self.observerclause))
        return tuple(nodelist)

    attr_names = ()

class StateClause(Node):
    def __init__(self, type, state):
        self.type = type
        self.state = state

    def children(self):
        nodelist = []
        for i, child in enumerate(self.state or []):
            nodelist.append(("state[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class EventClause(Node):
    def __init__(self, event):
        self.event = event

    def children(self):
        nodelist = []
        for i, child in enumerate(self.event or []):
            nodelist.append(("event[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class TransitionClause(Node):
    def __init__(self, transition):
        self.transition = transition

    def children(self):
        nodelist = []
        for i, child in enumerate(self.transition or []):
            nodelist.append(("transition[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class Transition(Node):
    def __init__(self, event, state1, state2):
        self.event = event
        self.state1 = state1
        self.state2 = state2

    def children(self):
        nodelist = []
        if self.event is not None: nodelist.append(("event", self.event))
        if self.state1 is not None: nodelist.append(("state1", self.state1))
        if self.state2 is not None: nodelist.append(("state2", self.state2))
        return tuple(nodelist)

    attr_names = ()



class EventIdentifier(Node):
    def __init__(self,identifier):
        self.identifier=identifier

    def children(self):
        nodelist = []
        if self.identifier is not None: nodelist.append(("identifier", self.identifier))
        return tuple(nodelist)

    attr_names=()

class StateIdentifier(Node):
    def ___init__(self,identifier):
        self.identifier=identifier

    def children(self):
        nodelist = []
        if self.identifier is not None : nodelist.append(("identifier", self.identifier))

    attr_names=()

class ComposedBlockClause(Node):
    def __init__(self,Block, ClassInstance):
        self.Block = Block
        self.ClassInstance = ClassInstance

    def children(self):
        nodelist = []
        if self.Block is not None : nodelist.append(("Block", self.Block))
        for i, child in enumerate(self.ClassInstance or []):
            nodelist.append(("ClassInstance[%d]" % i, child))
        return tuple(nodelist)

    attr_names=()

class ClassInstance(Node):
    def __init__(self, identifier):
        self.identifier = identifier

    def children(self):
        nodelist = []
        for i, child in enumerate(self.identifier or []):
            nodelist.append(("identifier[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class ClassIdentifier(Node):
    def __init__(self,identifier):
        self.identifier=identifier

    def children(self):
        nodelist = []
        if self.identifier is not None : nodelist.append(("identifier", self.identifier))
        return tuple(nodelist)

    attr_names=()

class SynchronizationClause(Node):
    def __init__(self, synchronization):
        self.synchronization = synchronization

    def children(self):
        nodelist = []
        for i, child in enumerate(self.synchronization or []):
            nodelist.append(("synchronization[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class Synchronization(Node):
    def __init__(self, macroEventDefinition):
        self.macroEventDefinition = macroEventDefinition

    def children(self):
        nodelist = []
        if self.macroEventDefinition is not None: nodelist.append(("macroEventDefinition", self.macroEventDefinition))
        return tuple(nodelist)

    attr_names = ()

class MacroEventDefinition(Node):
    def __init__(self, event, eventPath1, eventPathList):
        self.event = event
        self.eventPath1 = eventPath1
        self.eventPathList = eventPathList

    def children(self):
        nodelist = []
        if self.event is not None: nodelist.append(("event", self.event))
        if self.eventPath1 is not None: nodelist.append(("eventPath1", self.eventPath1))
        for i, child in enumerate(self.eventPathList or []):
            nodelist.append(("eventPathList[%d]" % i, child))

        return tuple(nodelist)

    attr_names = ()

class EventPath(Node):
    def __init__(self, identifier1, identifier2):
        self.identifier1 = identifier1
        self.identifier2 = identifier2

    def children(self):
        nodelist = []
        if self.identifier1 is not None: nodelist.append(("identifier1", self.identifier1))
        if self.identifier2 is not None: nodelist.append(("identifier2", self.identifier2))
        return tuple(nodelist)

    attr_names = ()
