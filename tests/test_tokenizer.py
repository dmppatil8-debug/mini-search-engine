from search.tokenizer import tokenize


def test_lowercase():
    result = tokenize("Python PYTHON")

    assert result == ["python", "python"]


def test_remove_punctuation():
    result = tokenize("Python, is powerful!")

    assert result == ["python", "powerful"]


def test_remove_stop_words():
    result = tokenize("the python is powerful")

    assert result == ["python", "powerful"]


def test_empty_text():
    result = tokenize("")

    assert result == []


def test_stop_words_only():
    result = tokenize("the is and or")

    assert result == []