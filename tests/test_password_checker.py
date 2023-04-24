import pytest
from lib.password_checker import PasswordChecker

"""
the password is 12 characters long
so we get True in return
by using 12 right away, we can save the step of testing for 8 because
if 8 is not true, 12 would not be true either
"""
def test_password_length_is_equal_8():
    password = PasswordChecker()
    assert password.check('12345678') == True

def test_password_length_is_more_than_8():
    password = PasswordChecker()
    assert password.check('1234567890123') == True

def test_password_length_is_false():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('Hi')
    error = str(e.value)
    assert error == 'Invalid password, must be 8+ characters.'