from lib.string_builder import *

def test_string_builder1():
    string1 = StringBuilder()
    string1.add('example string')
    result_size = string1.size()
    assert result_size == 14
    result_output = string1.output()
    assert result_output == 'example string'

def test_string_builder2():
    string = StringBuilder()
    string.add('Oberlad')
    string.add('stätter')
    result_size = string.size()
    assert result_size == 14
    result_output = string.output()
    assert result_output == 'Oberladstätter'

