import unittest
from ValidateBrackets import validate_brackets

class ValidateBracketsTests(unittest.TestCase):

    def test_validation_correct(self):

        self.assertTrue(validate_brackets(""))
        self.assertTrue(validate_brackets("()"))
        self.assertTrue(validate_brackets("()()"))
        self.assertTrue(validate_brackets("()[]"))
        self.assertTrue(validate_brackets("{}[]"))
        self.assertTrue(validate_brackets("(){}[]"))
        self.assertTrue(validate_brackets("[{}]"))
        self.assertTrue(validate_brackets("((){})"))
        self.assertTrue(validate_brackets("[{()}]"))

    def test_validation_incorrect(self):
        self.assertFalse(validate_brackets("("))
        self.assertFalse(validate_brackets("(]"))
        self.assertFalse(validate_brackets(")("))
        self.assertFalse(validate_brackets("{[}]"))
        self.assertFalse(validate_brackets("{[(})}"))

    def test_validation_error(self):
        with self.assertRaises(RuntimeError):
            validate_brackets("a")
            validate_brackets("[a]")


if __name__ == '__main__':
    unittest.main()