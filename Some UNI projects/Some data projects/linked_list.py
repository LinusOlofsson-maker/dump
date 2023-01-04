""" linked_list.py

Student: Linus Olofsson
Mail:Linus.Olofsson.4269@student.uu.se
Reviewed by: Mikael Johansson
Date reviewed: 06/10 - 22
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        pass

    def mean(self):               # Optional
        pass

    def remove_last(self):        # Optional
        pass

    def remove(self, x):          # Compulsory
        if self.first == None:
            return False
        f = self.first
        if f.data == x:            # Kollar om det är försrta
            self.first = f.succ
            return True
        while f.succ is not None:       # Kollar på f.succ tills den är None
            if f.succ.data == x:
                f.succ = f.succ.succ        # Om datan är den vi söker så omdirigerar vi den "två steg".
                return True
            f = f.succ
        return False

    def count(self, x):           # Optional
        pass

    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    def _to_list(self, f):
        if f is None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)

    def remove_all(self, x):      # Compulsory
        if x in self:
            self.remove(x)          # Rekrusivt tar vi bort alla steg för steg
            self.remove_all(x)
        else:
            return

    def __str__(self):            # Compulsary
        string = "()"
        for i in self:
            string = string.replace(")", f"{i}, )")         # Vi klipper helt enkelt bara in det sökta i strängen.
        string = string.replace(", )", ")")
        return string

   # def copy(self):               # Compulsary
   #     result = LinkedList()
   #     for x in self:
   #         result.insert(x)
   #     return result
    ''' Complexity for this implementation: 
        e(n), där n är längden av den totala listan.
    '''

    def copy(self):               # Compulsary
        res_rev = LinkedList()                           # Should be more efficient
        res_send = self.to_list()
        res_send.reverse()
        for i in range(len(res_send)):
            res_rev.insert(res_send[i])            # Behandlar endast första noden då den
        return res_rev

    ''' Complexity for this implementation:
        e(1), Detta då den endast kopierar första noden, med andra ord så behövs bara ett anropp göras. 
    '''

    def __getitem__(self, ind):   # Compulsory
        f = self.first
        for i in range(ind):
            f = f.succ
        return f.data


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __le__(self, other):
        if self.name <= other.name:                 # Less or equal för förklara för insert metoden ovan
            return True
        else:
            return False

    def __gt__(self, other):
        if self.name > other.name:                  # greater than för förklara för insert metoden ovan
            return True
        else:
            return False


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    lst.copy()
    # Test code:


if __name__ == '__main__':
    main()
