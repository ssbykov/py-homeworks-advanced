import pytest
from main import m_int

class TestFunctionsPytest:
    def setUp(self):
        print('Вызвали метов setUp')

    def teardown(self):
        print('Вызвали метод teardown')

   
    def test_m_int(self):
        assert m_int(2, 5) == 7