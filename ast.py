__author__ = 'deschancesdjomo'

class Node(object):
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

class BlockDecl(Node):
    def __init__(self, type, name, body):
        self.type = type
        self.name = name
        self.body =  body

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