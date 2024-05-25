def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 5
    print("Teste de adição passou")