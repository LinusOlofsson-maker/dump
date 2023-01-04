"""
Solutions to module 2 - A calculator
Student: Linus Olofsson
Mail:Linus.Olofsson.4269@student.uu.se
Reviewed by: Adam Pehrson
Reviewed date: 2022-09-19
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def fib(n, memory=None):
    if n >= 0 and n == int(n):
        if memory is None:
            memory = {0: 0, 1: 1}
        if n not in memory:
            memory[n] = fib(n - 1, memory) + fib(n - 2, memory)
        return memory[n]
    else:
        raise EvaluationError('ILLEGAL Action: Needs to be positive and integer\n Youre now banned from math!')


def fac(n):
    if n < 0 or n % 1 != 0:
        raise EvaluationError('ILLEGAL Action: Needs to be positive and integer\n Youre now banned from math!')
    else:
        result = math.factorial(n)
    return result


def log(n):
    if n <= 0:
        raise EvaluationError('ILLEGAL Action: Needs to be positive\n Youre now banned from math!')
    else:
        result = math.log(n)
    return result


def summing(list):
    result = sum(list)
    return result


def maxing(list):
    result = max(list)
    return result


def minimizing(list):
    result = min(list)
    return result


def mean(list):
    result = sum(list) / len(list)
    return result


def statement(wtok, variables):
    result = assignment(wtok, variables)
    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError("Invalid input")


def assignment(wtok, variables):
    result = expression(wtok, variables)
    while wtok.get_current() == "=":
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected variable name also It's python god damnit, not C#!")
    return result


def expression(wtok, variables):
    result = term(wtok, variables)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        if wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/'):
        if wtok.get_current() == '*':
            wtok.next()
            result *= factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            division = factor(wtok, variables)
            if division == 0:
                raise EvaluationError('ILLEGAL Action: Division by 0, Youre now banned from math!')
            result /= division
    return result


def factor(wtok, variables):
    fun_lib = {
        'sin': math.sin,
        'cos': math.cos,
        'exp': math.exp,
        'log': log,
        'fib': fib,
        'fac': fac
    }

    multifun_lib = {
        'min': minimizing,
        'max': maxing,
        'sum': summing,
        'mean': mean
    }

    if wtok.get_current() == '-':
        flip = -1
        wtok.next()
    else:
        flip = 1

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        wtok.next()

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()

        elif wtok.get_current() in {**fun_lib, **multifun_lib}:
            fun_save = wtok.get_current()
            wtok.next()
            if wtok.get_current() == '(':
                wtok.next()
                if fun_save in fun_lib:
                    result = fun_lib[fun_save](assignment(wtok, variables))
                elif fun_save in multifun_lib:
                    result = multifun_lib[fun_save](arglist(wtok, variables))
                wtok.next()
            else:
                raise SyntaxError('Expected "("')
        else:
            raise EvaluationError(f"{wtok.get_current()} is not regocnized as a variable or function name")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    else:
        raise SyntaxError(
            "Expected number or '('")

    return flip * result



def arglist(wtok, variables):
    result = [assignment(wtok, variables)]
    while wtok.get_current() == ",":
        wtok.next()
        result = result + [assignment(wtok, variables)]
    return result


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")

    variables = {"ans": 0.0, "E": math.e, "PI": math.pi, 'pi': math.pi,
                 'e': math.e}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ev:
                print("*** Evaluation error: ", ev)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")


if __name__ == "__main__":
    main()
