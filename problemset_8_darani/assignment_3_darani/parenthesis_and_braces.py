from lliststack import Stack


class ParenthesisAndBracesChecker:

    def __init__(self):
        self.stk_chars = Stack()

    def _check_delimiter(self, delimiter, left_delimiter, right_delimiter):
        if delimiter == right_delimiter:
            if self.stk_chars.peek() == left_delimiter:
                self.stk_chars.pop()
            else:
                raise WrongExpectedDelimiterException(delimiter)

    def analyze_text(self, input_text: str):
        for char in input_text:
            if char in "({[":
                self.stk_chars.push(char)
            self._check_delimiter(char, '(', ')')
            self._check_delimiter(char, '[', ']')
            self._check_delimiter(char, '{', '}')
        if not self.stk_chars.is_empty():
            raise UnbalancedDelimitersException(self.stk_chars)


class WrongExpectedDelimiterException(Exception):
    def __init__(self, delimiter):
        super().__init__(f'There is no left delimiter corresponding "{delimiter}"')


class UnbalancedDelimitersException(Exception):
    def __init__(self, stack_delimiters: Stack):
        first = True
        while not stack_delimiters.is_empty():
            if first:
                msg = f"Parenthesis and braces are unbalanced, remaining: {stack_delimiters.pop()}"
                first = False
            else:
                msg += f", {stack_delimiters.pop()}"
        super().__init__(f'Parenthesis and braces are unbalanced, remaining: [, (')


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
