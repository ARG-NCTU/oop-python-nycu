import example

def test_add():
    assert example.add(2, 3) == 5

def test_hello(capsys):
    obj = example.Example()
    obj.hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

