from spotlight.errors import STRING_ERROR
from .validator_test import ValidatorTest


class StringTest(ValidatorTest):
    def setUp(self):
        self.field = "test"
        self.string_error = STRING_ERROR.format(field=self.field)

    def test_string_rule_with_integer_expect_error(self):
        rules = {"test": "string"}
        data = {"test": 1}
        expected = self.string_error

        errors = self.validator.validate(data, rules)
        errs = errors.get(self.field)

        self.assertEqual(errs[0], expected)

    def test_string_rule_with_string_expect_no_error(self):
        rules = {"test": "string"}
        data = {"test": "hello world"}
        expected = None

        errors = self.validator.validate(data, rules)
        errs = errors.get(self.field)

        self.assertEqual(errs, expected)

    def test_valid_string_with_invalid_values_expect_false(self):
        invalid_strings = [True, False, -1, 0, 1, 2, [], {}]

        for invalid_string in invalid_strings:
            actual = self.validator.valid_string(invalid_string)
            self.assertEqual(actual, False)

    def test_valid_string_with_valid_values_expect_true(self):
        valid_strings = ["", "hello", "world", "0", "1", "!"]

        for valid_string in valid_strings:
            actual = self.validator.valid_string(valid_string)
            self.assertEqual(actual, True)