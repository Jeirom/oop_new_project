import pytest
from lessons_ex.lessons1 import Student

@pytest.fixture
def alisa():
    return Student('Alisa',5)

def test_init(alisa):
    assert alisa.name == 'Alisa'
    assert alisa.course == 5


#
# import pytest
#
#
# @pytest.fixture
# def developer_ivan():
#     return Developer('Ivan', 'Ivanov')
#
#
# def test_init(developer_ivan):
#     assert developer_ivan.name == 'Ivan'
#     assert developer_ivan.surname == 'Ivanov'
#
#
# def test_work(developer_ivan):
#     developer_ivan.work()
#     assert developer_ivan.is_working
#     assert not developer_ivan.is_on_vacation
#
#
# def test_vacation(developer_ivan):
#     developer_ivan.go_to_vacation()
#     assert not developer_ivan.is_working
#     assert developer_ivan.is_on_vacation