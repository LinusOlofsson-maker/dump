"""
Solutions to module 1
Student: Linus Olofsson
Mail:Linus.Olofsson.4269@student.uu.se
Reviewed by: Adam Pehrson
Reviewed date:2022-09-19
"""

import random
import time


def fib(n, memory=None):
    if n >= 0 and n == int(n):
        if memory is None:
            memory = {0: 0, 1: 1}
        if n not in memory:
            memory[n] = fib(n - 1, memory) + fib(n - 2, memory)
        return memory[n]


def power(x, n):  # Optional
    pass


def multiply(m, n):  # Compulsory
    if m < n:
        return multiply(n, m)
    elif n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)


def divide(t, n):  # Optional
    pass


def harmonic(n):  # Compulsory
    if 1 / n == 1:
        return 1
    return 1 / n + harmonic(n - 1)


def digit_sum(x):  # Optional
    pass


def get_binary(x):  # Optional
    pass


def reverse(s):  # Optional
    pass


def largest(a):  # Compulsory
    if len(a) == 1:
        return a[0]
    elif a[-1] <= a[0]:
        return largest(a[:-1])
    else:
        return largest(a[1:])


def count(x, s):  # Compulsory
    if len(s) == 0:
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:])  # + 1 => kollar hur många som gått in
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


def zippa(l1, l2):  # Compulsory

    if len(l1) > 0 or len(l2) > 0:
        return l1[:1] + l2[:1] + zippa(l1[1:], l2[1:])  # lägg ihop första elementen och
    if len(l1) == 0 and len(l2) == 0:                   # retunerar resterande lista
            return []                                   # Python är konstig, därför fungerar detta :D <3


def bricklek(f, t, h, n):  # Compulsory
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n - 1) + [f + '->' + t] + bricklek(h, t, f, n - 1)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    mult = multiply(5, 3)
    print('Multiplication:')
    print(mult)
    print(' ')

    print('Harmonic:')
    harm = harmonic(10)
    print(harm)
    print(' ')

    print('Largest:')
    lst = [5, 3, 7, 11, 4]
    L = largest(lst)
    print(L)
    print(' ')

    print('Counter:')
    x = 4
    s = [1, 4, 2, ['a', [[4], 3, 4]]]
    co = count(x, s)
    print(co)
    print(' ')

    print('Zipper:')
    l1 = [1, 3, 5]
    l2 = [2, 4, 6, 8, 10]
    zipper = zippa(l1, l2)
    print(zipper)
    print(' ')

    # start = time.perf_counter()
    print(bricklek('f', 't', 'h', 4))
    # elapsed = (time.perf_counter() - start)
    # print(elapsed)
    # print(' ')
    # tal = 3
    # start = time.perf_counter()
    # fibu = fib(tal)
    # elapsed = (time.perf_counter() - start)
    # print(f"För att räkna ut fibonatchital nmr: {tal} så tar det: {elapsed} sekunder för att få svaret: {fibu}")
    # print(' ')
    print('Bye!')


if __name__ == "__main__":
    main()

####################################################    

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 15: Time for bricklek with 50 bricks:
    As the minimum moves required to solve a ToH game is ((2**n) - 1) <=> 2exp(n)-1 where n = ammount of tiles and each
    move takes 1 second ==> 1.12589*e15 sec ==> 1.887649*e13 hours ==> 7.818749*e11 days ==> 2142123110 years! 
  
  
  
  
  
  Exercise 16: Time for Fibonacci:
        To calculate n = #           time:                increase:
        To calculate n = 5           time: 4.09e-6 sec    increase:
        To calculate n = 10          time: 5.58e-5 sec    increase:
        To calculate n = 15          time: 4.65e-5 sec    increase:
        To calculate n = 20          time: 4.47e-3 sec    increase:
        To calculate n = 25          time: 4.47e-2 sec    increase:
        To calculate n = 30          time: 0.508   sec    increase:
        To calculate n = 35          time: 5.70    sec    increase:
        To calculate n = 36          time: 9.05    sec    increase:
        To calculate n = 37          time: 14.5    sec    increase:
        To calculate n = 40          time: 41.5    sec    increase:
        To calculate n = 44          time: 449.2   sec <=> 7 min 29 sec
        To calculate n = 47          time: 1166.78 sec <=> 19min 26 sec
        To calculate n = 50          time: 4956.98 sec <=> 82 min 36 sec        
        
    
        Calculationsof t(n) = 1 + t(n-1)+t(n-2) ==> @ 50 sec: 5.622*e10 ==> 937140288.7 min ==> 15619004.81 h ==> 
            ==> 650791.86 days ==> 1782.99 years!  
        
            @ 100  1.580*e21 sec==> 2.63*e19 min ==> 4.39*e17 h ==> 
            ==> 1.8296*e16 days ==> 5.01*e13 years!  
  
  
  
  Exercise 19: Comparison sorting methods:
  
    **    insertion sort and merge sort    **  
    @ 10^6
        -> Insertion sort Worst case: t(n) = n(n+1)/2 => 5.0*e11 s ==> 15854.9 years
        
        -> Merge: t(n) = nlogn ==> 6000000 sec ==> 100000 min ==> 69.4 days
  
  @10^9
        -> Insertion sort Worst case: t(n) = n(n+1)/2 => 5.0*e17 sec ==> 1.5854*e10 years
        
        -> Merge: t(n) = nlogn ==> 9000000000 sec ==> 285.38 days
  
  Exercise 20: Comparison Theta(n) and Theta(n log n)
        -> As Theta(n) is a Linear function whenever n doubble the runtime doubbles, however when n doubbles the runtime
           more then doubbles. So to A will run faster then B when we take 2n.
           
           
           New comments from TA: 
           
           
           Excersise 20 och ex 19 needs to be redone. 
  
  
  
  Detta är förbättringen av vad som noteras som Exercise 19 & 20 tidigare, Nedan noteras dem som 20 & 21.
  
  
  Exercise 20: jämförelse av sorterings metoderna
        
        
        Använda e(n^2)/e(1000^2) <-- Detta motsvarar " Insertion sort"

        Använda e(n*log10(n))/e(1000log10(1000))  <-- Detta motsvarar " Merge sort"
  
        För att sortera 10e6 element med "Insertion sort" skulle det ta ungefär 11 dagar 
        medans med "Merge sort" tar det ca 30 minuter
  
        För att sortera 10e9 element med "Insertion sort" skulle det ta ungefär 31 dagar 
        medans med "Merge sort" tar det  ca 34 dagar 
    
  

  Exersise 21: Jämför Theta(n) & Theta(n log(n))
  
  
    Vi vet att A kan  lösa ett problem av storlek n på n sekunder. 
    Vi vet också att B är en algoritm av c*n*log10(n), där c är en konstant. 
    B löser också detta på 1 sekund då n = 10.  Hur stort måste n vara för att A ska vara snabbare än B? 
    
    Först för att hitta c:
    
    c = 1/(10*log10(10)) = 1/10 
    
    så för att A(t) < B(t):
    
    n < c*n*log10(n) 
    
    Vi vet redan att
        - V.L = 1
        - c = 1/10
    vilket ger:
    1/c < log10(n)
    10^(1/c) < n
    
    Detta innebär att n måste vara större än 10^10 innan A blir snabbare än B!
    
    Svar: n > 10^10 


"""
