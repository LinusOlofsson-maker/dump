""" bst.py

Student: Linus Olofsson
Mail: Linus.Olofsson.4269@student.uu.se
Reviewed by: Mikael Johansson
Date reviewed: 06/10 - 22
"""


from linked_list import LinkedList
# These imports are used to answer the Theoretical questions ONLY!
import random
import math
import statistics
from matplotlib import pyplot as plt



class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)

    def _height(self,n):                                # Kollar vänster och höger och adderar 1 för att ta reda på höjden
        if n is None:
            return 0
        left = 1 + self._height(n.left)
        right = 1 + self._height(n.right)
        if right < left:
            return left
        else:
            return right
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)                    # eftersom vänster är de mindre värderna
        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right,k)                   # Eftersom höger är de större värderna
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                res = r.right
                r = None
                return res
            elif r.right is None:  # Also easy case
                res = r.left
                r = None
                return res
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                smallest = r.right
                while smallest.left:                        # Kollar så om det finns mindre värden och lokaliserar det minsta.
                    smallest = smallest.left                # Vi söker helt enkelt efter " den minsta bland de största "
                r.key = smallest.key
                r.right = self._remove(r.right, smallest.key)

        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory

        string = self._str(self.root, "<>")

        string = string.replace(", >", ">")
        return string

    def _str(self, r, string):                                  # skapar en string o placerar in önskade värden.
        if r:
            string = self._str(r.left, string)
            string = string.replace(">", f"{r.key}, >")
            string = self._str(r.right, string)
        return string

    def to_list(self):                            # Compulsory
        lst = []
        for i in self:                                          # Eftersom vi kollar i self så fås allt i ordning.
            lst.append(i)
        return lst

    def to_LinkedList(self):                      # Compulsory
        linked = LinkedList()
        for i in self:                                          # skapar ett LinkedList objekt kör tillsätter.
            linked.insert(i)
        return linked
    # Här blir komplexiteten e(n) alltså man måste itterera över alla noder.


    def ipl(self):                                # Compulsory
        internal = self._ipl(self.root,0)                       # Ansettar noll som start längd.
        return internal

    def _ipl(self,r,x):
        if r is None:
            return 0
        else:
            x += 1                                             # Adderar 1 till längden och kollar på nästa steg Vänster sedan höger.
            return x + self._ipl(r.left,x) + self._ipl(r.right,x)

def random_tree(n):                               # Useful
    t = BST()
                                                            # Skapar träd och kör n antal ggr. .
    for i in range(0,n):
        tree = random.random()
        t.insert(tree)

    return t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    print(f"the list: {t.to_list()}")
    print(f"Internal steps: {t.ipl()}")
    print(f"height of tree: {t.height()}")
    print(f"remove 6 from tree: {t.remove(6)}")
    print(t)


    print('\nRandom Tree Beräkningar: ')
    print("Uträknad i Main:")
    n = 1000 # Itterationer
    N = 10  # Storlek på random träd
    x = range(1,n)
    ipl_list_mean = []
    for i in range(1,n):
        Tree = random_tree(i)
        medel_ipl = Tree.ipl() / Tree.size()
        ipl_list_mean.append(medel_ipl)
        #print(i)
#        print(f"[Size Tree]: {Tree.size()} [Height]: {Tree.height()} [IPL mean]: {medel_ipl }")

    theoretical = 1.39*math.log2(n)
    median = statistics.median(ipl_list_mean)
    y_theory = [1.39 * math.log2(N) for N in x]

    fig, ax = plt.subplots()
    ax.plot(x, ipl_list_mean,'b--')
    ax.plot(x, y_theory,'k')
    ax.legend([f'Random Tree observations with itterations: {n} and size: {n}',f'Theoretical values [1.39*log2(n)] with n: {n}'])
    ax.grid()
    ax.set_xlabel(f'Mean value of all IPL mean: {sum(ipl_list_mean)/n} and \nFrom the theoretical with n = {n}: {theoretical}\nMax IPL: {max(ipl_list_mean)} and Min IPL: {min(ipl_list_mean)}')
    #fig.canvas.draw()

    print(f"\nMean value of all IPL mean: {sum(ipl_list_mean)/n} and the median value is: {median} with n = {n}\nFrom the theoretical with n = {n}: {theoretical}\nItterating over {n} Random Trees with Max IPL: {max(ipl_list_mean)} and Min IPL: {min(ipl_list_mean)}")
    plt.show()
if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes! Genom att använda en For loop for i in self sedan adderar man 1 bara i en separat variabel. 
2. computing height? Nja, generellt Nej. Har man ett " Worst case senario " träd med grenar åt 1 håll, så går det att itterar över det med en for-loop
3. contains? Går super bra, vi leatar ändå efter 1 specifikt värde, vilket inte tar hänsyn till position! 
4. insert? Nej i de absolut flesta fallen, endast funktionabellt då man har ett träd med bara "vänster" alternativt "höger" grenar, alltså bara växande eller fallande
5. remove? Nej i de absolut flesta fallen, endast funktionabellt då man har ett träd med bara "vänster" alternativt "höger" grenar, alltså bara växande eller fallande 




Results for ipl of random trees
===============================


Random Tree Beräkningar: 
########################################################################################################################
Mean value of all IPL mean: 7.607000000000002 for n = 100
From the theoretical with n = 100: 9.234960103786866
Itterating over 100 Random Trees
########################################################################################################################

Vi försökte köra med mer itterationer:

########################################################################################################################
Mean value of all IPL mean: 3.4438214000044174 for n = 10
From the theoretical with n = 10: 4.617480051893433
Itterating over 1000000 Random Trees with Max IPL: 5.5 and Min IPL: 2.9
########################################################################################################################

sedan försökte vi med Mycket mer itterationer:

########################################################################################################################
Mean value of all IPL mean: 3.4436304800342374 and the median value is: 3.3 for n = 10
From the theoretical with n = 10: 4.617480051893433
Itterating over 10000000 Random Trees with Max IPL: 5.5 and Min IPL: 2.9
########################################################################################################################

Se även grafen vid körning. 

"""
