# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 21:07:57 2017

@author: Krishna
"""

from pyparsing import *
import re

UPTO, WORDS, AND, OR = map(CaselessKeyword, "upto words and or".split())
keyword = UPTO | WORDS | AND | OR
LBRACE,RBRACE = map(Suppress, "{}")
integer = pyparsing_common.integer()

word = ~keyword + Word(alphas)
upto_expr = Group(LBRACE + UPTO + integer("numberofwords") + WORDS + RBRACE)

class Node(object):
    def __init__(self, tokens):
        self.tokens = tokens
#        print 23
#        print self.tokens

    def generate(self):
        pass

class LiteralNode(Node):
    def generate(self):
        print type(self.tokens[0])
        return "(%s)" % re.escape(self.tokens[0])
    def __repr__(self):
        return repr(self.tokens[0])

class AndNode(Node):
    def generate(self):
        tokens = self.tokens[0]
#        print (tokens)
        return '.*'.join(t.generate() for t in tokens[::2])

    def __repr__(self):
        return ' AND '.join(repr(t) for t in self.tokens[0].asList()[::2])

class OrNode(Node):
    def generate(self):
        tokens = self.tokens[0]
        return '|'.join(t.generate() for t in tokens[::2])

    def __repr__(self):
        return ' OR '.join(repr(t) for t in self.tokens[0].asList()[::2])

class UpToNode(Node):
    def generate(self):
        tokens = self.tokens[0]
#        print (tokens)
        ret = tokens[0].generate()
        word_re = r"\s+\S+"
        space_re = r"\s+"
        for op, operand in zip(tokens[1::2], tokens[2::2]):
            # op contains the parsed "upto" expression
            ret += "((%s){0,%d}%s)" % (word_re, op.numberofwords, space_re) + operand.generate()
        return ret

    def __repr__(self):
        tokens = self.tokens[0]
        ret = repr(tokens[0])
        for op, operand in zip(tokens[1::2], tokens[2::2]):
            # op contains the parsed "upto" expression
            ret += " {0-%d WORDS} " % (op.numberofwords) + repr(operand)
        return ret

IMPLICIT_AND = Empty().setParseAction(replaceWith("AND"))
#SPACE = Empty()

phrase_expr = infixNotation(word.setParseAction(LiteralNode),
        [
        (upto_expr, 2, opAssoc.LEFT, UpToNode),
        (AND|IMPLICIT_AND, 2, opAssoc.LEFT, AndNode),
#        (SPACE, 2, opAssoc.LEFT, LiteralNode),
        (OR, 2, opAssoc.LEFT, OrNode),
        ])

tests = """\
        xyz
        xyz AND {upto 3 words} abc
        xyz there are {upto 3 words} and then {upto 4 words} here
        xyz {upto 4 words} def""".splitlines()
        
tests1 = """
        xyz abc
        """.splitlines()

for t in tests:
    t = t.strip()
    if not t:
        continue
#    print(type(t))
#    print (2423)
    try:
        parsed = phrase_expr.parseString(t)
    except ParseException as pe:
        print(' '*pe.loc + '^')
        print(pe)
        continue
    print(parsed)
    print type(parsed[0])
    print(parsed[0].generate())
    print