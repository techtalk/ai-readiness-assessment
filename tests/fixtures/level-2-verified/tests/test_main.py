from wordcount import count_words


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_single_word():
    assert count_words("hello") == 1


def test_count_words_whitespace_separated():
    assert count_words("the quick brown fox") == 4


def test_count_words_newlines_count_as_separators():
    assert count_words("one\ntwo\nthree") == 3
