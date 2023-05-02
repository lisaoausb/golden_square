"""
1. Describe Problem
As a user
I check my grammar and want to know how much of the document has been checked in %.
2. Design Solution

class GrammarStats:
    def __init__(self):
        pass
    def check(self, text):
        self.text = text
        #returns true if text begins with a capital letter and ends with a
        #sentence-ending punctuation mark. false otherwise.

    def percentage_good(self):
        returns percentage of texts checked so far that passed the check 
        defined in check method. Number 55 = 55%. 

3. Create Tests

def test_error_for_empty_string():
    with pytest.raises(Exception) as e:
        result = check('')
    error_message = str(e.value)
    assert error_message == 'No text given'

def test_text_has_a_capital_is_True():
    result = check('Hello')
    assert result == True

def test_text_has_a_capital_is_False():
    result = check('hello')
    assert result == False


def test_text_has_valid_punctuation_is_True():
    result = check('hello.')
    assert result == True

def test_text_has_valid_punctuation_is_False():
    result = check('hello')
    assert result == False

def test_text_has_capital_but_no_punctuation():
    result = check('Hello')
    assert result == False

def test_text_has_punctuation_but_no_capital():
    result = check('hello!')
    assert result == False

def test_text_has_punctuation_and_capital():
    result = check('Hello!')
    assert result == True

def test_progress_no_capital_no_punctuation():
    result = percentage_good()
    assert result == 0

def test_progress_capital_only():
    result = percentage_good()
    assert result == 50

def test_progress_punctuation_only():
    result = percentage_good()
    assert result == 50

def test_progress_capital_and_punctuation():
    result = percentage_good()
    assert result == 100

4. Code solution
"""