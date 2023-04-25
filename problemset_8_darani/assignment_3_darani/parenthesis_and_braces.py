from lliststack import Stack


class ParenthesisAndBracesChecker:

    def __init__(self):
        ...

    def analyze_text(self, input_text: str):
        ...


if __name__ == '__main__':
    checker = ParenthesisAndBracesChecker()

    unbalanced_1 = "foo( bar { baz }]"
    try:
        checker.analyze_text(unbalanced_1)
        assert False, "should raise an exception"
    except Exception as e:
        print(e)

    unbalanced_2 = "foo( bar { baz [ }]"
    try:
        checker.analyze_text(unbalanced_2)
        assert False, "should raise an exception"
    except Exception as e:
        print(e)

    unbalanced_3 = "foo([( bar { baz [qux] })"
    try:
        checker.analyze_text(unbalanced_3)
        assert False, "should raise an exception"
    except Exception as e:
        print(e)

    unbalanced_2 = "foo( bar { baz [qux] })"
    checker.analyze_text(unbalanced_2)
