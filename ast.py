__author__ = 'deschancesdjomo'
import sys

class Node(object):
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass


    def show(self, buf=sys.stdout, offset=0, _my_node_name=None):
        lead = ' ' * offset
        if _my_node_name is not None:
            buf.write('\n' + lead + ' <' + _my_node_name + '>: ')
        else:
            buf.write('{ ' +lead + self.__class__.__name__+ ': [')

        if self.attr_names:
            vlist = [getattr(self, n) for n in self.attr_names]
            attrstr = ', '.join('%s' % v for v in vlist)
            buf.write(attrstr)


        for (child_name, child) in self.children():
            child.show(
                buf,
                offset=offset + 2,
                _my_node_name=child_name)


class ModelDecl(Node):
    def __init__(self, classlist, block):
        self.type = "model"
        self.block = block
        self.classlist = classlist

    def children(self):
        nodelist = []
        if self.block is not None : nodelist.append(("classlist", self.classlist))
        if self.block is not None : nodelist.append(("block", self.block))

        return tuple(nodelist)

    attr_names=()

class BlockDecl(Node):
    def __init__(self, type, name, body):
        self.type = type
        self.name = name
        self.body = body

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("blocktype", self.type))
        if self.name is not None: nodelist.append(("blockname", self.name))
        if self.body is not None: nodelist.append(("blockbody", self.body))
        return tuple(nodelist)

    attr_names = ()



class BlockBody(Node):
    def __init__(self, firstclause, eventclause, thirdclause):
        self.firstclause = firstclause
        self.eventclause = eventclause
        self.thirdclause = thirdclause

    def children(self):
        nodelist = []
        if self.firstclause is not None: nodelist.append(("firstclause", self.firstclause))
        if self.eventclause is not None: nodelist.append(("eventclause", self.eventclause))
        if self.thirdclause is not None: nodelist.append(("thirdclause", self.thirdclause))
        return tuple(nodelist)

    attr_names = ()


class ComposedBlockClause(Node):
    def __init__(self,Block, ClassInstance):
        self.Block = Block
        self.ClassInstance = ClassInstance

    def children(self):
        nodelist = []
        if self.Block is not None : nodelist.append(("block", self.Block))
        for i, child in enumerate(self.ClassInstance or []):
            nodelist.append(("classInstance[%d]" % i, child))
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
        if self.event is not None: nodelist.append(("synchro", self.eventPathList))
        return tuple(nodelist)

    attr_names = ()

class EventPath(Node):
    def __init__(self, id, values):
        self.id = id
        self.values = values

    def children(self):
        nodelist = []
        if self.id is not None: nodelist.append(("id", self.id))
        if self.values is not None: nodelist.append(("values", self.values))
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
        if self.type is not None : nodelist.append(("objecttype", self.type))
        if self.values is not None : nodelist.append(("objectvalues", self.values))
        return tuple(nodelist)

    attr_names = ()
