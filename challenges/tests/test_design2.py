from lib.design_2 import *

# Test 1: we test if a string starts with a capital & ends in a full stop, in which case in returns True.

def test_check_grammar_with_capital_punctuation():
    result = check_grammar('Hello.')
    assert result == True

# Test 2: we test if a string starts with a capital and does not end in a FS/QM/EM (test all three punctuation marks) and returns False.
def test_check_grammar_with_capital_no_punctuation():
    result = check_grammar("Hello")
    assert result == False

# Test 3: we test if a string does not start with a capital and does end in a FS/QM/EM (test all three punctuation marks) and returns False.
def test_check_grammar_no_capital_with_punctuation():
    result = check_grammar("hello.")
    assert result == False

# Test 4: we test if a string does not start with a capital and does not end in a FS/QM/EM (test all three punctuation marks) and returns False.
def test_check_grammar_no_capital_no_punctuation():
    result = check_grammar('hello')
    assert result == False