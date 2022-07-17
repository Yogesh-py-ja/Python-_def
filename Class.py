# Example : a set of integers as class

class intset(object):

    """ an intset ia a set of integers
        the value is represented uy a list of ints,self.vals
        each int in the set accurs in self.vals exactly once """

    def __init__ (self):

        """ Create an empty set of integers """

        self.vals = []


    def insert (self,e):

        """ Assume e is an integer and inserts e in to self"""

        if not e in self.vals:
            self.vals.append(e)

    def member(self,e):

        """ Assumes e is an integer
        returns TRUE id e is in self,and false otherwise""""
        return e in self.vals

s =(intset())
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
s.remove(3)
print(s)










    
