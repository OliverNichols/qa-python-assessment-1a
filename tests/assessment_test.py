from programs import questions


def test_one():
    assert questions.one("hi", "hello") == "hello"
    assert questions.one("three", "two") == "three"
    assert questions.one("three", "hello") == "three hello"
    assert questions.one("echo", "print") == "print"
    assert questions.one("fire", "rib") == "fire"


def test_two():
    assert questions.two("bertclivebert") == "clive"
    assert questions.two("xxbertfridgebertyy") == "fridge"
    assert questions.two("xxBertfridgebERtyy") == "fridge"
    assert questions.two("xxbertyy") == ""
    assert questions.two("xxbeRTyy") == ""


def test_three():
    assert questions.three(3) == "fizz"
    assert questions.three(10) == "buzz"
    assert questions.three(15) == "fizzbuzz"
    assert questions.three(8) == "null"
    assert questions.three(75) == "fizzbuzz"


def test_four():
    assert questions.four("55 72 86") == 14
    assert questions.four("15 72 80 164") == 11
    assert questions.four("555 72 86 45 10") == 15
    assert questions.four("98 63 34 1 13") == 17
    assert questions.four("98 107 415") == 17


def test_five():
    assert questions.five("Jeff,random.py,False,1445") == ["Jeff"]
    assert questions.five(
        "Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445"
    ) == ["Jeff"]
    assert questions.five(
        "Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445"
    ) == ["Bert", "Jeff"]
    assert questions.five(
        "Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445"
    ) == ["Bert", "Jeff"]
    assert (
        questions.five(
            "Bert,files.py,True,1447,Bert,tests.py,True,1318,Jeff,app.py,True,1445"
        )
        == []
    )


def test_six():
    assert questions.six("ceiling") == True
    assert questions.six("believe") == True
    assert questions.six("glacier") == False
    assert questions.six("height") == False
    assert questions.six("receive") == True


def test_seven():
    assert questions.seven("Hello") == 2
    assert questions.seven("hEelLoooO") == 6
    assert questions.seven("WhitEboarD") == 4
    assert questions.seven("as") == 1
    assert questions.seven("pass") == 1


def test_eight():
    assert questions.eight(1) == 1
    assert questions.eight(3) == 6
    assert questions.eight(4) == 24
    assert questions.eight(6) == 720
    assert questions.eight(8) == 40320


def test_nine():
    assert questions.nine("This is a Sentence", "s") == 4
    assert questions.nine("This is a Sentence", "S") == 8
    assert questions.nine("Fridge for sale", "z") == -1
    assert questions.nine("I love Python", "L") == -1
    assert questions.nine("I LOVE PYTHON", "L") == 2


def test_ten():
    assert questions.ten("The", 2, "h") == True
    assert questions.ten("AAbb", 1, "b") == False
    assert questions.ten("Hi-There", 10, "e") == False
    assert questions.ten("HEY", 2, "e") == True
    assert questions.ten("on-premise", 3, "-") == True
