#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        t = len(sentence), None
        return t
    t = len(sentence), sentence[0]
    return t
