from lib.greet import *

def test_greet_lisa():
    result = greet("Lisa")
    assert result == "Hello, Lisa!"