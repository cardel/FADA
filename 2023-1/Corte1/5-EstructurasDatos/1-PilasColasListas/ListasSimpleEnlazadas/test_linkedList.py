from linkedList import LinkedList


def test_insert():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    assert objLinkedlist.head.value == 5
    assert objLinkedlist.head.ptrNext is None

    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    assert objLinkedlist.head.ptrNext.value == 10
    assert objLinkedlist.head.ptrNext.ptrNext is not None

    assert objLinkedlist.head.ptrNext.ptrNext.value == 20
    assert objLinkedlist.head.ptrNext.ptrNext.ptrNext is None


def test_getIndex():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    objLinkedlist.insert(30)

    assert objLinkedlist.getIndex(0) == 5
    assert objLinkedlist.getIndex(1) == 10
    assert objLinkedlist.getIndex(2) == 20
    assert objLinkedlist.getIndex(3) == 30

    try:
        objLinkedlist.getIndex(4)
    except OverflowError:
        assert True
    except Exception:
        assert False


def test_delete():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    objLinkedlist.insert(30)

    objLinkedlist.delete(5)
    assert objLinkedlist.getIndex(0) == 10

    objLinkedlist.delete(20)
    assert objLinkedlist.getIndex(0) == 10
    assert objLinkedlist.getIndex(1) == 30

    try:
        objLinkedlist.delete(40)
    except ReferenceError:
        assert True
    except Exception:
        assert False
