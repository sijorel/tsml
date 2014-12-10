__author__ = 'deschancesdjomo'
##
#  Transform pseudo_automota into final automata
#  Synchornized product is computed  here
#  The output should be used for model checking
#  The output can be printed
#
# Input : pseudo_automata
# Output : automata
##
##
# Transform pseudo automata into automata
# Some properties can be verified here
# The output is used to compute the synchronized product
#
# Input: pseudoAutomata
# Output: automata
##

import automata
import pseudoAutmata
#from pseudoAtomata import Node

class pAutmata:

    def __init__(self, model):
        self.model = model




    def searchInstance(self,block):
        result=[]
        for c in block.classInstance:
            for i in c[1]:
                result= result+[[i, c[0]]]
        return result

    def searchBlock(self,nom):
         for (k, block)in self.model.items():
            if block.name==nom:
                return block
         return None



    def searchEvent(self,B, synchro):
        S=synchro.split("&")
        for s in S:
            s1=s.split(".")
            if s1[0]==B :
                return s1[1]
        return None

    def transformVector(self, E, S):

        if E[0]!=None:
            if len(E[0])>1:
                S.insert(0,E[1])

                return self.transformVector(E[0],S)
            else:
                S.insert(0,E)
        else:
            S.insert(0,E[1])
            S.insert(0,E[0])

        return S

    def synchronisationVector(self, result, B, synchro,blockB):
        i=-1
        resultE=list(result)
        for S in synchro:
            i=i+1
            event=self.searchEvent(B,S[1])
            resultE[i]=[resultE[i]]+[event]

            event=None

        return list(resultE)

    def modifBlock(self, input, block):
        outputS=[]

        outputE=[]
        outputT=[]


        for s in input[0]:
            S=[]
            outputS.append(self.transformVector(s,S))


        for e in input[1]:
            S=[]
            outputE.append(self.transformVector(e,S))


        for t in input[2]:
            t1=automata.transition()
            t1.event=[]
            t1.state1=[]
            t1.state2=[]
            E=[]
            S1=[]
            S2=[]
            t1.event=(self.transformVector(t[0],E))

            states=t[1]
            t1.state1=(self.transformVector(states[0],S1))
            t1.state2=(self.transformVector(states[1],S2))

            outputT.append(t1)

        block.synchronisation=None
        block.state=outputS
        block.event=outputE
        block.transition=outputT
        return block

    def ps(self, A,B,E):
        i=[A[3],B[3]]
        candidates= list([i])

        S=[]
        T=[]
        while candidates != [] :

            for s in candidates:
                candidates.remove(s)

                S=S+[s]

                for e in E:

                        a=0
                        b=0
                        for transitionA in A[2]:
                            if e[0] == transitionA[0]:
                                a=1
                                for transitionB in B[2]:
                                    if e[1] == transitionB[0]:
                                        b=1
                                        stateA=transitionA[1]
                                        stateB=transitionB[1]
                                        if stateA[0]==s[0] and stateB[0]==s[1]:
                                            T=T+[[e,[s,[stateA[1], stateB[1]]]]]
                                            if [stateA[1], stateB[1]] not in S and [stateA[1], stateB[1]] not in candidates:
                                                candidates=candidates+[[stateA[1], stateB[1]]]

                        for transition in A[2]:
                            if e[0]==transition[0] and b==0:
                                    state= transition[1]
                                    if state[0]==s[0]:
                                            T=T+[[e,[s,[state[1], s[1]]]]]
                                            if [state[1], s[1]] not in S and [state[1], s[1]] not in candidates:
                                                candidates=candidates+[[state[1], s[1]]]



                        for transition in B[2] :
                                    if e[1] == transition[0]and a==0:
                                        state= transition[1]
                                        if state[0]==s[1]:
                                            T=T+[[e,[s,[s[0], state[1]]]]]
                                            if [s[0], state[1]] not in S and [s[0], state[1]] not in candidates:
                                                 candidates=candidates+[[s[0], state[1]]]

        return [list(S ),list(E),list(T),list( i)]


    def fixpointCalculation(self, block):
        i=0
        E=[]

        result=[]
        instances= list(self.searchInstance(block))


        i=0
        for instance in instances:

            blockB=self.searchBlock(instance[1])
            if blockB!=None :
                if blockB.synchronisation ==None:
                    if i==0 :
                        j=0
                        result=[blockB.state,blockB.event,blockB.transition,blockB.state[0]]
                        for S in block.synchronisation:
                            event=self.searchEvent(instance[0],S[1])
                            blockB=self.searchBlock(instance[1])
                            E.append(event)
                            j=j+1


                    else:

                            A=[blockB.state,blockB.event,blockB.transition,blockB.state[0]]

                            E= list(self.synchronisationVector(E,instance[0],block.synchronisation,blockB))

                            result=list(self.ps(result,A,E))


                else:
                    self.fixpointCalculation(blockB)
                    # modification BlockB
            i=i+1

        return result

    def parcourModel (self):
        result=[]

        for (k, block)in self.model.items():

            if block.synchronisation is not None:
                result= self.fixpointCalculation(block)
                # modification de block
                # output synchronisation
                block=self.modifBlock(list(result),block)
                print block.synchronisation






def main():
    pass

if __name__ == '__main__':
    model = {}
    #type(model)

    # creation objet pseudo automate
    pa=pseudoAutmata.blockClass()
    pa.name="window"
    pa.synchronisation=None # test avec synchronisation null
    pa.state=["openW", "closeW"]
    pa.event=["openingW", "closingW"]
    t=[["openingW",["closeW","openW"]], ["closingW",["openW","closeW"]]]
    pa.transition=t


    synchronisation=[["Aop","A.opening"],["Bop","B.opening"],["Cop", "C.opening"],["Dop","D.opening"],["closing","A.closing&B.closing&C.closing"]]

    pa1=pseudoAutmata.blockClass()
    pa1.synchronisation=synchronisation

    #declaration class istance pour pa1

    #type(classInstance)
    classInstance=[["door",["A", "B", "C", "D"]] ]
    pa1.classInstance=classInstance
    pa1.event=["Aop","Bop","Cop","Dop","closing", "closingW"]
    pa1.name="DoubleDoor"

    #declaration block door
    pa2=pseudoAutmata.blockClass()
    pa2.name="door"
    pa2.synchronisation=None
    pa2.state=["close", "open"]
    pa2.event=["opening", "closing"]
    t=[["opening",["close","open"]], ["closing",["open","close"]]]
    pa2.transition=t

    #declaration d'une autre classe
    c=pseudoAutmata.blockClass()
    c.name="mon test"

    model={"block":pa1, "class": pa2,"class1": pa}
    pAuto=pAutmata(model)

    pAuto.parcourModel()




