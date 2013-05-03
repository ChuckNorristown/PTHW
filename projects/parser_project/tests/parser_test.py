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




