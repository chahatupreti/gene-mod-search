# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 13:28:58 2017

@author: Krishna
"""

####################################
# DESCRIPTION : 
# In the first part of this code, I am basically assigning a grammar to my Human Readble Rules (HRR).
# I am using Pyparsing to do this. I first declare line directives, and then operators. I then decalre all of them 
# as 'keyword' and also assign the precedence priority for them. Then I define the grammar for a phrase_word, phrase_term,
# phrase_expression, line_term (i.e. a sub-rule) and finally for the entire rule (line_contents_expr). I have tested 
# the parsing on 2 rules - one is fictional and is made to check the various parts and second is a simpe real rule. 
####################################


from pyparsing import (CaselessKeyword, Word, alphanums, nums, MatchFirst, quotedString, 
    infixNotation, Combine, opAssoc, Suppress, pyparsing_common, Group, OneOrMore, ZeroOrMore)
import pprint
log = open('E:\F DRIVE\M.Tech\parsing\parsing log.txt','w')

LINE_CONTAINS, LINE_STARTSWITH, LINE_ENDSWITH = map(CaselessKeyword,
    """LINE_CONTAINS LINE_STARTSWITH LINE_ENDSWITH""".split()) # put option for LINE_ENDSWITH. Users may use, I don't presently

NOT, AND, OR = map(CaselessKeyword, "NOT AND OR".split())
BEFORE, AFTER, JOIN = map(CaselessKeyword, "BEFORE AFTER JOIN".split())

lpar=Suppress('{') 
rpar=Suppress('}')

keyword = MatchFirst([LINE_CONTAINS, LINE_STARTSWITH, LINE_ENDSWITH, NOT, AND, OR, 
                      BEFORE, AFTER, JOIN]) # declaring all keywords and assigning order for all further use

phrase_word = ~keyword + (Word(alphanums + '_'))

upto_N_words = Group(lpar + 'upto' + pyparsing_common.integer('numberofwords') + 'words' + rpar)
upto_N_chars = Group(lpar + 'upto' + pyparsing_common.integer('numberofchars') + 'characters' + rpar)

phrase_term = Group(OneOrMore(phrase_word) + ZeroOrMore(((upto_N_words) | ZeroOrMore(upto_N_chars)) + OneOrMore(phrase_word))) | quotedString # changed phrase_word to OneOrMore(phrase_word) to allow multi-word phrases
# phrase-term

# want to know if there is a way to just say that the phrase_term can contain both types of elements instead of
# having to give the exact grammar for it as  p_w+upto+p_W


phrase_expr = infixNotation(phrase_term,
                            [
                             ((BEFORE | AFTER | JOIN), 2, opAssoc.LEFT,), # (opExpr, numTerms, rightLeftAssoc, parseAction)
                             (NOT, 1, opAssoc.RIGHT,),
                             (AND, 2, opAssoc.LEFT,),
                             (OR, 2, opAssoc.LEFT),
                            ],
                            lpar=Suppress('{'), rpar=Suppress('}')
                            ) # structure of a single phrase with its operators

line_term = Group((LINE_CONTAINS | LINE_STARTSWITH | LINE_ENDSWITH)("line_directive") + 
                  Group(phrase_expr)("phrase")) # basically giving structure to a single sub-rule having line-term and phrase
line_contents_expr = infixNotation(line_term,
                                   [(NOT, 1, opAssoc.RIGHT,),
                                    (AND, 2, opAssoc.LEFT,),
                                    (OR, 2, opAssoc.LEFT),
                                    ]
                                   ) # grammar for the entire rule/sentence

sample1 = """
LINE_CONTAINS transfected gene BEFORE {sirna} AND gene AND LINE_STARTSWITH Therefore we
"""
sample11 = """
LINE_CONTAINS sentence one BEFORE {sentence2 AND sentence3} AND LINE_STARTSWITH Therefore we
"""
sample2 = """
LINE_CONTAINS abcd {upto 4 words} xyzw {upto 3 words} pqrs BEFORE something else
"""
sample3 = """
LINE_STARTSWITH Here we AND LINE_CONTAINS {phrase number 1} AND phrase 2 BEFORE {phrase number 3} AND resin JOIN gene
"""

#line_contents_expr.runTests(sample2)
#print (line_contents_expr.numberofwords)
#line_contents_expr.runTests(sample2)

#line_contents_expr.runTests(sample2)
parsed = line_contents_expr.parseString(sample2)
#print (parsed[0].asDict())
print (type(parsed))
#pd = parsed.dump()
#print pd
#log.write(pd)
#log.write('\n')
#c=pd.split()
#for c1 in c:
#    log.write(c1)


    
regex_sample1 = 're.search(^Therefore we(?=transfected gene.*?sirna))(?=gene)'    
regex_sample11 = 're.search(^Therefore we(?=sentence one.*?(sentence2|sentence 3)))'
# other option - sentence one.*?(?:sentence two.*?sentence three|sentence three.*?sentence two)
regex_sample2 = 're.search(abcd ([\w]+\s*){0,4}xyzw([\w]+\s*){0,3}pqrs.*?something else)'
#regex_sample3 = 're.search(^Here we.*?phrase 2.*?phrase number 3) and re.search(phrase number 1)'    
regex_sample3 = 're.search(^Here we(?=phrase 2.*?phrase number 3)(?=phrase number 1)(?=resin([- ])?gene)'
    




    
    
    
    
#print 3
#pprint.pprint(parsed)

#print(type(parsed))
#print parsed.asList()
#print (parsed.phrase_term)
#print (parsed.phrase.numberofwords)