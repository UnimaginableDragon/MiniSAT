class Lit:   #literal class
    def __init__(self, x=0):
        self.x=x
    def __eq__(self, other):
        return self.x==other.x
    def __ne__(self, other):
        return self.x!=other.x
    def __lt__(self, other):
        return self.x < other.x
    def mkLit(self,var,sign=False):
        p = Lit()
        p.x = var + var + int(sign)
        return p
    def __invert__(self):
        q = Lit()
        q.x= self.x ^ 1
        return q
    def __xor__(self, p, b):
        q = Lit()
        q.x = p.x ^ int(b)
        return q
    def __xor__(self, b):
        q = Lit()
        q.x = self.x ^ int(b)
        return q
    def sign(self,p):
        return p.x & 1

    def var(self,p):
        return p.x >> 1
    def sign(self):
        return self.x &1
    def var(self):
        return self.x >> 1

    def toInt(self):
        return self.x
    def toLit(self, i):
        q = Lit()
        q.x=i
        return q

class Clause:
    def __init__(self,ps, use_extra=False, learnt=False):
        self.mark = 0
        self.learnt = learnt
        self.has_extra = learnt | use_extra
        self.reloced = 0
        self.size =ps.size()
        self.lbd = 0
        self.removable = 1
        self.simplified = 0
        self.act=None
        self.touched=None
        self.rel=None
        self.data_lit=[]
        for i in range(size):
            data_lit.apppend(ps[i])

        if(self.has_extra):
            if(self.learnt):
                self.act=0
                self.touched=0
            else:  #calculateAbstraction
                abstraction = 0
                for i in range(size):
                    abstraction |= 1 << (data_lit[i].x & 31);
                self.abs = abstraction;

    def last(self):
        return self.data_lit[self.size-1]

    def relocation(self):
        return self.rel
    def relocate(self,c):
        self.reloced=1
        self.rel=c

    def __getitem__(self, item):
        return self.data_lit[item]

    def activity(self):
        return self.act
    def abstraction(self):
        return self.abs

    def subsumes(self,other):
        if ((other.size < self.size) or (self.abs & ~other.abs) != 0):
            return "lit_error"

        ret = None# undefined
        c=self.data_lit
        d=other.data_lit

        for i in range(self.size):
            for j in range (self.size):
                if(c[i]==d[j]):
                    break
                elif ( ret is None && c[i]== ~ d[j]):
                    ret = c[i]
                    break;

        return ret

class Solver:
    def __init__(self):
        self.model = None # if problem is satisfied result is here
        self.conflict   = None # If the problem is unsatisfied  the vector represents the final conflict clause expressed in assumptions
        #Mode of operation
        self.drup_file = None
        self.step_size= None
        self.step_size_dec = None
        self.time = None
        self.var_decay  = None
        self.clause_decay = None
        self.random_var_freq = None
        self.random_seed = None
        

    def addClause(self, ps):
        None
    def addEmptyClause(self):
        None
    def addClause(self,p): # add a unity clause
        None
    def addClause(self,p,q): # add a binary clause
        None
    def addCause(self,p,q,r):  # add a ternary clause
        NOne

    def simplify(self): # remove already satisfied clauses
        None

    def solve(self,assumps): # search for a model that resepects given set of assumptions
        None

    def solve(self): # search without assumptions
        None

    def okay(self): # False means solver is in a conflicting state
        None

    def toDimacs(self,file,assumps): # write CNF to file in DIMACS format
        None

    def toDimacs(self,file,p):
        None

    def toDimacs(self,file,p,q):
        None
    def toDimacs(self,file,p,q,r):
        None

    def setPolarity(self,v,b): # declare which polarity the decision heuristics should use
        None

    def setDecisionVar(self,v,b): #declare if a variable is eligible for decision heuristic
        None

    def value(self,x):
        None # The current value  of a variable,literal,.

    def modelValue(self,x):
        None
    # The value of a variable in the last model.The last call to solve must have been satisfiable.

    def nAssigns(self):
        None
    # The current number of assigned literals.
    def nClauses(self):  # The current number of original clauses.
        None

    def nLearnts(self): # The current number of Learnt clauses
        None
    def nVars(self): # the current number of vaiables
        None
    def nFreeVars(self):
        None






