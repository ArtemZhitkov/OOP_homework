def test_smartphone(smartphone1):
    assert smartphone1.name == "Xiaomi Redmi Note 11"
    assert smartphone1.description == "1024GB, Синий"
    assert smartphone1.price == 31000.0
    assert smartphone1.quantity == 14
    assert smartphone1.efficiency == 90.3
    assert smartphone1.model == "Note 11"
    assert smartphone1.memory == 1024
    assert smartphone1.color == "Синий"
