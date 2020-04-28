# this program divides equation in monomials,
# finds indexes(like a,b,c in quadratic or linear equation),
# adds them up and solves with formulas

import math
import cmath

symbols = ('+', '-', '=', '^', 'x', '.')
splitsymbols = ('+', '-', '=')
helpMsg = "This app helps to solve equation\n" \
          "it is still in development and some signs like brackets, '/' and '*' are still unavailable\n" \
          "if there is not any number after =, that means that equation equals 0\n" \
          "for example '5x+8-9x^2=' is the same like '5x+8-9x^2=0' "


def appendIndex(indl, monomial, isEqPassed):
    try:
        index = 0.0
        arr_num = 0
        monomial_def = ''
        last_float_pos = 0
        # 1 GET INDEX
        # if sign is missing, add '+'
        if monomial[0] != '+' and monomial[0] != '-':
            monomial = '+' + monomial
        # if index is missing, index is 1
        if not monomial[1].isdigit():
            if monomial[1] != 'x':
                print('error with monomial, the second digit is some special digit')
                return []
            else:
                index = 1.0
                last_float_pos = 1
                monomial_def = monomial[last_float_pos:]
        else:
            # get index
            count = 0
            for ch in monomial:
                if ch != '+' and ch != '-' and ch != '.' and not ch.isdigit():
                    last_float_pos = count
                    index = float(monomial[:last_float_pos])
                    monomial_def = monomial[last_float_pos:]
                    break
                if count == len(monomial) - 1 and ch.isdigit():
                    index = float(monomial)
                    arr_num = 0
                    break
                count += 1

        if isEqPassed:
            index = -index
        # 2 GET A, B OR C IN EQUATION
        # get index in array to append
        if monomial_def == '':
            arr_num = 0
        elif monomial_def == 'x':
            arr_num = 1
        elif monomial_def == 'x^2':
            arr_num = 2
        else:
            print('error with monomial: ', monomial_def)
            return []
        # 3 APPEND
        indl[arr_num] += index
        return indl
    # 4 if index is incorrect
    except ValueError as msg:
        print('error')
        print(msg)


def is_correct_equation(eq):
    for ch in eq:
        if not ch in symbols and not ch.isdigit():
            return False
    if '=' not in eq:
        return False
    return True


def get_indexes(eq):
    indexes = [0.0, 0.0, 0.0, 0.0]
    is_eq_pass = False
    last_monomial_pos = 0
    this_pos = 0
    for ch in eq:
        mon = ''
        if this_pos == len(eq) - 1:
            mon = eq[last_monomial_pos:]
            indexes = appendIndex(indexes, mon, is_eq_pass)
            if not indexes:
                return []
        elif ch in splitsymbols:
            mon = eq[last_monomial_pos:this_pos]
            indexes = appendIndex(indexes, mon, is_eq_pass)
            if not indexes:
                return []
            if indexesa;
                
            # append indexes
        if ch == '=':
            is_eq_pass = True
            last_monomial_pos = this_pos + 1
        elif ch == '+' or ch == '-':
            last_monomial_pos = this_pos
        this_pos += 1
    return indexes


def solveLinear(indexes):
    return [-indexes[0] / indexes[1]]


def solveQuadratic(indexes):
    a = indexes[2]
    b = indexes[1]
    c = indexes[0]
    # print("D = b\u00b2 - 4ac")
    discriminant = b ** 2 - 4 * a * c
    # print("D = {0}".format(discriminant))
    if discriminant == 0:
        # print('x = -b / 2a')
        return [-b / (2 * a)]


    elif discriminant > 0:
        # print("x = (-b - \u221aD) / 2a")
        root = math.sqrt(discriminant)
    else:
        # print("x = (-b - i\u221aD) / 2a")
        root = cmath.sqrt(discriminant)
    return [-b - root / (2 * a), -b + root / (2 * a)]


def solve_equation(eq):
    if not is_correct_equation(eq):
        print("equation is incorrect")
        return []
    indexes = get_indexes(eq)
    if not indexes:
        return []
    if indexes[1] == 0.0 and indexes[2] == 0.0 and indexes[0] != 0.0:
        print('x \u2208 \u2205')
        return []
    elif indexes[1] == 0.0 and indexes[2] == 0.0 and indexes[0] == 0.0:
        print('x \u2208 \u211d')
        return []
    if indexes[2] == 0.0:
        return solveLinear(indexes)
    else:
        return solveQuadratic(indexes)


def print_results(slist):
    if not slist:
        pass
    else:
        for solve in slist:
            print('x = ', solve, ' ')


def main():
    print("input the equation(quadratic or linear), or input 'help':")
    eq = input()
    if eq == 'help':
        print(helpMsg)
    else:
        solvelist = solve_equation(eq)
        print_results(solvelist)


main()
