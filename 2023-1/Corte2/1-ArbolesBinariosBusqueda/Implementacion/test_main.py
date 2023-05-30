from ArbolBB import ArbolBB
import random

def test_flat():
  lst = [1,[1,3],[[[[[[[3]]],5]]]]]
  arbol1 = ArbolBB(5,None,None)
  assert arbol1.flat(lst) == [1,1,3,3,5]



def test_format():
  arbol1 = ArbolBB(5,None,None)
  assert "5" == arbol1.__format__()

  arbol2 = ArbolBB(8,
          ArbolBB(7,
                  ArbolBB(4, ArbolBB(1,None,None),ArbolBB(6,None,None)),
                  None
                  ),
          ArbolBB(11,
                  ArbolBB(9, ArbolBB(8,None,None),ArbolBB(10,None,None)),
                  ArbolBB(12,None,None)
                  ))
  
  assert "(8 (7 (4 1 6) ) (11 (9 8 10) 12))" == arbol2.__format__()
  

def test_creation():
  arbol1 = ArbolBB(5,
            ArbolBB(4,
                    ArbolBB(4,
                            ArbolBB(1,None,None),
                            ArbolBB(4,None,None)
                            ),
                    None
                    ),
            ArbolBB(7,
                  ArbolBB(6, ArbolBB(5,None,None),ArbolBB(7,None,None)),
                  ArbolBB(8,None,None)
                  )
          )
  arbol1.set_father(None)

  assert [1,4,4,4,5,5,6,7,7,8] == arbol1.innorder_search()  


def test_minmax():
  arbol1 = ArbolBB(5,
          ArbolBB(4,
                  ArbolBB(4,
                          ArbolBB(1,None,None),
                          ArbolBB(4,None,None)
                          ),
                  None
                  ),
          ArbolBB(7,
                ArbolBB(6, ArbolBB(5,None,None),ArbolBB(7,None,None)),
                ArbolBB(8,None,None)
                )
        )
  
  arbol1.set_father(None)

  assert 1 == arbol1.minimum()
  assert 8 == arbol1.maximum()           

def test_search():
  arbol1 = ArbolBB(8,
            ArbolBB(7,
                    ArbolBB(4, ArbolBB(1,None,None),ArbolBB(6,None,None)),
                    None
                    ),
            ArbolBB(11,
                    ArbolBB(9, ArbolBB(8,None,None),ArbolBB(10,None,None)),
                    ArbolBB(12,None,None)
                    ))
  arbol1.set_father(None)
  assert 4 == arbol1.search(4).key
  assert None is arbol1.search(13)



def test_successor():
  arbol1 = ArbolBB(8,
              ArbolBB(7,
                      ArbolBB(4, ArbolBB(1,None,None),ArbolBB(6,None,None)),
                      None
                      ),
              ArbolBB(11,
                      ArbolBB(9, ArbolBB(8,None,None),ArbolBB(10,None,None)),
                      ArbolBB(12,None,None)
                      ))
  arbol1.set_father(None)

  assert [1,4,6,7,8,8,9,10,11,12] == arbol1.innorder_search()
  assert 12 == arbol1.successor(11)
  assert 11 == arbol1.successor(10)
  assert 8 == arbol1.successor(8)
  assert 10 == arbol1.successor(9)

def test_insert():
  arbol1 = ArbolBB(
    8,
    ArbolBB(4,
            ArbolBB(3,ArbolBB(1,None,None),None),
            ArbolBB(7,None,None)
            ),
    ArbolBB(10,
            None,
            ArbolBB(12,None,None)
            )
  )
  assert "(8 (4 (3 1 ) 7) (10  12))" == arbol1.__format__()
  arbol1.insertion(5)
  assert "(8 (4 (3 1 ) (7 5 )) (10  12))" == arbol1.__format__()
  arbol1.insertion(9)
  assert "(8 (4 (3 1 ) (7 5 )) (10 9 12))" == arbol1.__format__()
  arbol1.insertion(8)
  assert "(8 (4 (3 1 ) (7 5 )) (10 (9 8 ) 12))" == arbol1.__format__()

  ord = [200]
  arbol3 = ArbolBB(200,None,None)
  for i in range(0,1000):
    rnd = random.randrange(0,10000)
    ord.append(rnd)
    arbol3.insertion(rnd)

  ord.sort()
  assert ord == arbol3.innorder_search()

def test_elimination():
  arbol1 = ArbolBB(
    12,
    ArbolBB(10, ArbolBB(3,ArbolBB(1,None,None),ArbolBB(5,None,None)),None),
    ArbolBB(16,ArbolBB(13,None,None),ArbolBB(18,None,None))
  )
  arbol1.set_father(None)
  assert "(12 (10 (3 1 5) ) (16 13 18))" == arbol1.__format__()

  arbol1.elimitation(1)
  assert "(12 (10 (3  5) ) (16 13 18))" == arbol1.__format__()

  arbol1.elimitation(3)
  assert "(12 (10 5 ) (16 13 18))" == arbol1.__format__()

  arbol1.elimitation(12)
  assert "(13 (10 5 ) (16  18))" == arbol1.__format__()

