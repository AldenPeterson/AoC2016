import unittest

from day05 import Checker

class CheckerTest(unittest.TestCase):

    def test_hash_from_inputs(self):
        checker = Checker()
        self.assertEqual(
            checker._hex_hash_from_inputs('abc', 3231929),
            '00000155f8105dff7f56ee10fa9b9abd'
        )

    def test_hex_hash_matches(self):
        checker = Checker()
        self.assertTrue(checker.hex_hash_matches('00000155f8105dff7f56ee10fa9b9abd'))
        self.assertFalse(checker.hex_hash_matches('0000155f8105dff7f56ee10fa9b9abd'))

    def test_door_char_from_match(self):
        checker = Checker()
        self.assertEqual(checker.door_char_from_match('00000155f8105dff7f56ee10fa9b9abd'), '1')

    @unittest.skip("Part One")
    def test_get_door_password_part_1(self):

        checker = Checker()
        self.assertEqual(checker.get_door_password_part1('abc'), '18f47a30')

        # run with wrong input, find real input
        self.assertEqual(checker.get_door_password_part1('ojvtpuvg'), '4543c154')

    def test_update_door_password(self):
        checker = Checker()
        self.assertEqual(checker._update_door_password('aaaaaaaa', 'b', 4), 'aaaabaaa')

    @unittest.skip("Part Two")
    def test_get_door_password_part_2(self):

        checker = Checker()
        # self.assertEqual(checker.get_door_password_part2('abc'), '05ace8e3')
        self.assertEqual(checker.get_door_password_part2('ojvtpuvg'), '1050cbbd')

