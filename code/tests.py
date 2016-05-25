import to_test


def test_gen_io():
    assert to_test.gen_io().read() == "Hello world"
