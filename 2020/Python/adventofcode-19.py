import re

import helper

def Substitute(all_rules, rule: str) -> str:

    ret = ""

    for r in rule:

        if (r.isdigit()):
            ret += "(" + Substitute(all_rules, all_rules[int(r)]) + ")"
        elif (r == "|"):
            ret += "|"
        elif (r == '"a"'):
            ret += "a"
        elif (r == '"b"'):
            ret += "b"

    return ret

def part1() -> int:

    # raw data
    data = helper.getData("19")

    # data to be split in rules and words to match with
    rules = []
    words = []
    read_words = False

    # process data
    for d in data:

        if (d == ""):
            read_words = True
        elif (read_words):
            words.append(d)
        elif (not read_words):
            s = d.split(": ")
            rules.append( (int(s[0]), s[1]) )

    # sort (for index), split every single item in rule and set start rule
    rules.sort(key = lambda x: x[0])
    all_rules = [r[1].split(" ") for r in rules]
    start_rule = all_rules[0]

    # reguar expression from substiution 
    regex = Substitute(all_rules, start_rule)
    matches = 0

    # count and return matches
    for w in words:

        if (w in [e.group() for e in re.finditer(regex, w)]):
            matches += 1

    return matches

print("solution for part 1: {}".format(part1()))
