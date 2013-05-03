from nose.tools import *
from ex49 import parser

def test_peek():

    test_list = [('noun', 'princess')]
    result = parser.peek(test_list)
    assert_equal(result, 'noun')


    test_list = [('verb', 'go'),
                ('noun', 'princess'),
                ('direction', 'east')]
    result = parser.peek(test_list)
    assert_equal(result, 'verb')

    test_list = []
    result = parser.peek(test_list)
    assert_equal(result, None)

def test_match():

    test_list = [('noun', 'princess')]
    test_expecting = 'noun'
    result = parser.match(test_list, test_expecting)
    assert_equal(result, ('noun', 'princess'))

    test_list = [('verb', 'go'),
                ('noun', 'princess'),
                ('direction', 'east')]
    test_expecting = 'verb'
    result = parser.match(test_list, test_expecting)    
    assert_equal(result, ('verb', 'go'))

    test_list = [('verb', 'go'),
                ('noun', 'princess'),
                ('direction', 'east')]
    test_expecting = 'stop'
    result = parser.match(test_list, test_expecting)    
    assert_equal(result, None)

    test_list = []
    test_expecting = 'stop'
    result = parser.match(test_list, test_expecting)
    assert_equal(result, None)

def test_verb():

    test_list = [('verb', 'go')]
    result = parser.parse_verb(test_list)
    assert_equal(result, ('verb', 'go'))

    test_list = [('verb', 'go'),
                ('direction', 'west')]
    result = parser.parse_verb(test_list)
    assert_equal(result, ('verb', 'go'))

    test_list = [('stop', 'the'),
                ('stop', 'of'),
                ('verb', 'go'),
                ('direction', 'west')]
    result = parser.parse_verb(test_list)
    assert_equal(result, ('verb', 'go'))

    test_list = [('stop', 'the'),
                ('stop', 'of')]
    assert_raises(parser.ParserError, parser.parse_verb, test_list)

    assert_raises(parser.ParserError, parser.parse_verb, [])

def test_object():
    test_list = [('noun', 'princess')]
    result = parser.parse_object(test_list)
    assert_equal(result, ('noun', 'princess'))

    test_list = [('direction', 'east')]
    result = parser.parse_object(test_list)
    assert_equal(result, ('direction', 'east'))

    test_list = [('stop', 'in'),('direction', 'east')]
    result = parser.parse_object(test_list)
    assert_equal(result, ('direction', 'east'))

    assert_raises(parser.ParserError, parser.parse_object, [])

def test_subject():

    test_list = [('verb', 'eat'), ('stop', 'the'), ('noun', 'princess')]
    test_subj = ('noun', 'bear')
    result = parser.parse_subject(test_list, test_subj)
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'princess')

def test_sentence():
    test_list = [('stop', 'a'),('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'princess')]
    result = parser.parse_sentence(test_list)
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'princess')

    test_list = [('verb', 'shoot'), ('stop', 'the'), ('noun', 'bear')]
    result = parser.parse_sentence(test_list)
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'shoot')
    assert_equal(result.object, 'bear')

    test_list = [('direction', 'east'), ('stop', 'the'), ('noun', 'bear')]
    assert_raises(parser.ParserError, parser.parse_sentence, test_list)


    




