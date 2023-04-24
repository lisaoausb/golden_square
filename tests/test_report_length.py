from lib.report_length import *

def test_report_length_oberladstaetter():
    result = report_length("Oberladstaetter")
    assert result == 'This string was 15 characters long.'