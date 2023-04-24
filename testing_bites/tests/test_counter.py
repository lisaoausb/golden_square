from lib.counter import *

def test_the_counter1():
    counter = Counter()
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 2 so far."

def test_the_counter2():
    counter2 = Counter()
    counter2.add(1)
    counter2.add(3)
    counter2.add(5)
    result = counter2.report()
    assert result == "Counted to 9 so far."

def test_the_counter_minus():
    counter = Counter()
    counter.add(1)
    counter.add(3)
    counter.add(-6)
    result = counter.report()
    assert result == "Counted to -2 so far."