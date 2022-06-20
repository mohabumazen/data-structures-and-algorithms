import pytest
from Data_Structures.Linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip.llist_zip import zip_lists


def test_zip_lists(llist_test_1, llist_test_2):
    assert str(zip_lists(llist_test_1, llist_test_2)) == f'< {1} > -> < {5} > -> < {3} > -> < {9} > -> < {2} > -> NULL'


@pytest.fixture
def llist_test_1():
    ll1 = LinkedList()
    ll1.append(5)
    ll1.append(9)

    return ll1


@pytest.fixture
def llist_test_2():
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(3)
    ll2.append(2)

    return ll2


