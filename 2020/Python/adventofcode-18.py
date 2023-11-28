#!/usr/bin/env python

import re

import helper

def PlusPrecedence(term) -> str:

    # find plus terms
    plus_terms = re.findall("\d+ \+ \d+", term)

    while (len(plus_terms) > 0):

        for pt in plus_terms:
            value = eval(pt)
            term = term.replace(pt, str(value))

        plus_terms = re.findall("\d+ \+ \d+", term)

    return term

# returns evaluated expression (string), regular precedences will be ignored
def EvalExpressionWithoutPrecedences(term: str, plus_precedence: bool) -> int:

    # part 2/plus_precedence
    if plus_precedence:
        term = PlusPrecedence(term)

    # add bracket for each value found in string
    expression = ""
    number_brackets = len(re.findall("\d+", term))

    for _ in range(0, number_brackets):
        expression += "("

    # envelop each value with brackets for left to right precedence
    ss = term.split(" ")

    for e in ss:
        expression += str(e + ")") if (bool(re.match("\(*\d+\)*", e))) else str(e)

    return eval(expression)

def EvalExpressionWithPrecedences(term: str, plus_precedence: bool) -> int:

    # find inner terms surrounded by brackets
    inner_terms = re.findall("\(([^()]*)\)", term)

    for it in inner_terms:
        # evaluate and replace value with former term
        value = EvalExpressionWithPrecedences( it, plus_precedence )
        term = term.replace("(" + it + ")", str(value))

    # find outer terms surrounded by brackets
    outer_terms = re.findall("\(([^()]*)\)", term)

    for ot in outer_terms:
        # evaluate and replace value with former term
        value = EvalExpressionWithPrecedences( ot, plus_precedence )
        term = term.replace("(" + ot + ")", str(value))

    return EvalExpressionWithoutPrecedences(term, plus_precedence)

def part1() -> int:
    data = helper.getData("18")
    ret = 0

    for d in data:
        ret += EvalExpressionWithPrecedences(d, False)

    return ret

def part2() -> int:
    data = helper.getData("18")
    ret = 0

    for d in data:
        value = EvalExpressionWithPrecedences(d, True)
        #print("{} = {}".format(d, value))
        ret += value

    return ret

# main

print("solution for part 1: {}".format(part1()))
print("solution for part 2: {}".format(part2()))
