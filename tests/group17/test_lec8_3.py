def test_intSet():
    print("Testing intSet...")
    s = intSet()
    assert str(s) == "{}"

    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert str(s) == "{3,4}"

    assert s.member(3)
    assert not s.member(5)

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    try:
        s.remove(3)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "3 not found"

    print("intSet tests passed.\n")

test_intSet()
