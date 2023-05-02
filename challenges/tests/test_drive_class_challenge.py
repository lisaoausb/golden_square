import pytest
from lib.drive_class_challenge import *

def test_error_for_empty_string():
    grammar_check = GrammarStats()
    with pytest.raises(Exception) as e:
        result = grammar_check.check('')
    error_message = str(e.value)
    assert error_message == 'No text given'

# def test_text_has_a_capital_is_True():
#     grammar_check = GrammarStats()
#     result = grammar_check.check('Hello')
#     assert result == True

# def test_text_has_a_capital_is_False():
#     grammar_check = GrammarStats()
#     result = grammar_check.check('hello')
#     assert result == False

# def test_text_has_valid_punctuation_is_True():
#     grammar_check = GrammarStats()
#     result = grammar_check.check('hello.')
#     assert result == True

# def test_text_has_valid_punctuation_is_False():
#     grammar_check = GrammarStats()
#     result = grammar_check.check('hello')
#     assert result == False

def test_text_has_no_capital_and_no_punctuation():
    grammar_check = GrammarStats()
    result = grammar_check.check('hello')
    assert result == False

def test_text_has_capital_but_no_punctuation():
    grammar_check = GrammarStats()
    result = grammar_check.check('Hello')
    assert result == False

def test_text_has_punctuation_but_no_capital():
    grammar_check = GrammarStats()
    result = grammar_check.check('hello!')
    assert result == False

def test_text_has_punctuation_and_capital():
    grammar_check = GrammarStats()
    result = grammar_check.check('Hello!')
    assert result == True

def test_progress_where_half_is_False():
    grammar_check1 = GrammarStats()
    grammar_check1.check('Hello')
    grammar_check1.check('Hello.')
    grammar_check1.check('yeah okay')
    grammar_check1.check('Yes!')
    grammar_check1.check('Where you at?')
    grammar_check1.check('no!!!!!')
    result = grammar_check1.percentage_good()
    assert result == "50%"

def test_progress_where_all_correct():
    grammar_check3 = GrammarStats()
    grammar_check3.check('Hello.')
    result = grammar_check3.percentage_good()
    assert result == "100%"

def test_progress_where_75_false():
    grammar_check2 = GrammarStats()
    grammar_check2.check('Hello!')
    grammar_check2.check('no, mate')
    grammar_check2.check('missing')
    grammar_check2.check('Whatever')
    result = grammar_check2.percentage_good()
    assert result == "25%"

def test_progress_where_no_words_checked():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.percentage_good()
    error = str(e.value)
    assert error == 'N/A'
