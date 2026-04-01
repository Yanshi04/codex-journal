from django.test import TestCase
from django.core.exceptions import ValidationError
from bestiary.models import Monster, BeastsGroup, HowToWin, validate_letters_and_spaces

class BestiaryModelTests(TestCase):
    def test_validator_with_valid_string(self):
        # string should not raise an error
        try:
            validate_letters_and_spaces("Grave Hag")
        except ValidationError:
            self.fail("validate_letters_and_spaces raised ValidationError unexpectedly!")

    def test_validator_with_invalid_string(self):
        # invalid string with numbers should raise an error
        with self.assertRaises(ValidationError):
            validate_letters_and_spaces("Nekker123")

    def test_beasts_group_str_method(self):
        # tests the string representation of beastsgroup
        group = BeastsGroup(group_name = "Necrophages")
        self.assertEqual(str(group), "Necrophages")

    def test_how_to_win_str_method(self):
        # tests the string representation of howtowin
        item = HowToWin(item_name = "Igni Sign")
        self.assertEqual(str(item), "Igni Sign")
