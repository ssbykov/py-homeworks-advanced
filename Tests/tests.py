import pytest
from main import *


class TestFunctionsPytest:
    def setup(self):
        print('Вызвали метов setUp')

    def teardown(self):
        print('Вызвали метод teardown')


    def test_find_people(self):
        for document in documents:
            assert find_people(documents, document["number"]) == document["name"]

    def test_find_document_directory(self):
        for key, directory in directories.items():
            for doc_number in directory:
                assert find_document_directory(directories, doc_number) == key