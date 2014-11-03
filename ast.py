__author__ = 'deschancesdjomo'
import sys
class Node(object):
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

    def show(self, buf=sys.stdout, offset=0, attrnames=False, nodenames=False, _my_node_name=None):
        lead = ' ' * offset
        if nodenames and _my_node_name is not None:
            buf.write(lead + self.__class__.__name__+ ' <' + _my_node_name + '>: ')
        else:
            buf.write(lead + self.__class__.__name__+ ': ')

        if self.attr_names:
            if attrnames:
                nvlist = [(n, getattr(self,n)) for n in self.attr_names]
                attrstr = ', '.join('%s=%s' % nv for nv in nvlist)
            else:
                vlist = [getattr(self, n) for n in self.attr_names]
                attrstr = ', '.join('%s' % v for v in vlist)
            buf.write(attrstr)

        for (child_name, child) in self.children():

            child.show(
                buf,
                offset=offset + 2,
                attrnames=attrnames,
                nodenames=nodenames,
                _my_node_name=child_name)



class ModelDecl(Node):
    def __init__(self, classlist, block):
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
        if self.type is not None: nodelist.append(("type", self.type))
        if self.name is not None: nodelist.append(("name", self.name))
        if self.body is not None: nodelist.append(("blockbody", self.body))
        return tuple(nodelist)

    attr_names = ()


class BasicBlockBody(Node):
    def __init__(self, stateclause, eventclause, transitionclause):
        self.stateclause = stateclause
        self.eventclause = eventclause
        self.transitionclause = transitionclause

    def children(self):
        nodelist = []
        if self.stateclause is not None: nodelist.append(("stateclause", self.stateclause))
        if self.eventclause is not None: nodelist.append(("eventclause", self.eventclause))
        if self.transitionclause is not None: nodelist.append(("transitionclause", self.transitionclause))
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
    def __init__(self, classname, identifier):
        self.identifier = identifier
        self.classname = classname

    def children(self):
        nodelist = []
        if self.classname is not None : nodelist.append(("classname", self.classname))
        for i, child in enumerate(self.identifier or []):
            nodelist.append(("identifier[%d]" % i, child))
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

class Synchronization(Node):
    def __init__(self, event, eventPathList):
        self.event = event
        self.eventPathList = eventPathList

    def children(self):
        nodelist = []
        if self.event is not None: nodelist.append(("event", self.event))
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


class ParamList(Node):
    def __init__(self, params):
        self.params = params

    def children(self):
        nodelist = []
        for i, child in enumerate(self.params or []):
            nodelist.append(("params[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class ID(Node):
    def __init__(self, name):
        self.name = name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name',)

class ObjectDecl(Node):
    def __init__(self, type, values):
        self.type = type
        self.values = values

    def children(self):
        nodelist = []
        if self.type is not None : nodelist.append(("type", self.type))
        if self.values is not None : nodelist.append(("values", self.values))
        return tuple(nodelist)

    attr_names = ()
