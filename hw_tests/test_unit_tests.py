# import sys
# sys.path.append("G:/python/netology/py-homeworks-advanced/hw_tests")
from main import find_people, documents, m_int
import unittest


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('Вызвали метов сетап')

    def tearDown(self) -> None:
        print('Вызвали метов даун')

    # @patch.object(find_people, 'document_number')
    # def test_find_people(self):
    #     for number in documents['number']:
    #         document_number = number
    #         self.assertEqual(find_people(document_number), documents[number])

    def test_m_int(self):
        self.assertEqual(m_int(2, 5), 7)