from hashmap import HashMap


def test_add_initially_empty():
    # arrange
    hash_map = HashMap()
    # act
    hash_map.add(3, "Foo")
    hash_map.add(8, "Bar")
    # assert
    assert hash_map.value_of(3) == "Foo", "should have added \"Foo\""
    assert hash_map.value_of(8) == "Bar", "should have added \"Bar\""


def test_add_alreading_existing_element():
    # arrange
    hash_map = HashMap()
    # act
    hash_map.add(3, "Foo")
    hash_map.add(3, "Bar")
    # assert
    assert hash_map.value_of(3) == "Bar", "should have replaced \"Foo\" with \"Bar\""


def test_add_reash():
    # arrange
    hash_map = HashMap()
    # act
    hash_map.add(3, "Foo")
    hash_map.add(1, "Bar")
    hash_map.add(5, "Sar")
    hash_map.add(4, "Tar")
    hash_map.add(13, "Nam")
    hash_map.add(2, "Laf")
    hash_map.add(7, "Pel")
    hash_map.add(6, "Cis")
    # assert
    assert hash_map.value_of(3) == "Foo", "should have added \"Foo\""
    assert hash_map.value_of(1) == "Bar", "should have added \"Bar\""
    assert hash_map.value_of(5) == "Sar", "should have added \"Sar\""
    assert hash_map.value_of(4) == "Tar", "should have added \"Tar\""
    assert hash_map.value_of(13) == "Nam", "should have added \"Nam\""
    assert hash_map.value_of(2) == "Laf", "should have added \"Laf\""
    assert hash_map.value_of(7) == "Pel", "should have added \"Pel\""
    assert hash_map.value_of(6) == "Cis", "should have added \"Cis\""


def test_remove_existing_element():
    # arrange
    hash_map = HashMap()
    hash_map.add(3, "Foo")
    hash_map.add(5, "Bar")
    # act
    value = hash_map.remove(3)
    # assert
    try:
        hash_map.value_of(3)
        assert False, "should have raised IndexError"
    except Exception as e:
        assert type(e) is IndexError, "should have raised IndexError"
    assert value == "Foo", "should have removed \"Foo\""


def test_remove_non_existing_element():
    # arrange
    hash_map = HashMap()
    hash_map.add(3, "Foo")
    # act
    exception = None
    try:
        value = hash_map.remove(5)
    except Exception as e:
        exception = e
    # asssert
    assert exception is not None, "should have raised an Exception"
    assert type(exception) is IndexError, "should have raise an IndexError"


if __name__ == "__main__":
    test_add_initially_empty()
    test_add_alreading_existing_element()
    test_add_reash()
    test_remove_existing_element()
    test_remove_existing_element()
