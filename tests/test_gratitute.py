from lib.gratitute import Gratitudes

"""
Initially, we'll get 'Be grateful for: '
followed by nothing, as we have an empty list
"""
def test_empty_list():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == 'Be grateful for: '

def test_adding_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("Health")
    gratitude.add("Air to breathe")
    result = gratitude.format()
    assert result == 'Be grateful for: Health, Air to breathe'