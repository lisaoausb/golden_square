from lib.check_codeword import *

def test_check_codeword():
    result1 = check_codeword("horse")
    assert result1 == 'Correct! Come in.'
    result2 = check_codeword("hose")
    assert result2 == 'Close, but nope.'
    result3 = check_codeword("cow")
    assert result3 == 'WRONG!'