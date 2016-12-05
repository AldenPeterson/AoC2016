import unittest

from part01 import _encrypted_name, decode_shifted_room, _shift_string, _checksum, _sector_id, _convert_encrypted_name_to_characters, is_real_room


class part01_test(unittest.TestCase):

    def test_checksum(self):

        self.assertEqual(_checksum('aaaaa-bbb-z-y-x-123[abxyz]'), 'abxyz')
        self.assertEqual(_checksum('a-b-c-d-e-f-g-h-987[abcde]'), 'abcde')

        self.assertEqual(_checksum('not-a-real-room-404[oarel]'), 'oarel')
        self.assertEqual(_checksum('totally-real-room-200[decoy]'), 'decoy')

    def test_encrypted_name(self):
        self.assertEqual(_encrypted_name('aaaaa-bbb-z-y-x-123[abxyz]'), 'aaaaa-bbb-z-y-x')
        self.assertEqual(_encrypted_name('a-b-c-d-e-f-g-h-987[abcde]'), 'a-b-c-d-e-f-g-h')

        self.assertEqual(_encrypted_name('not-a-real-room-404[oarel]'), 'not-a-real-room')
        self.assertEqual(_encrypted_name('totally-real-room-200[decoy]'), 'totally-real-room')

    def test_sector_id(self):
        self.assertEqual(_sector_id('aaaaa-bbb-z-y-x-123[abxyz]'), '123')
        self.assertEqual(_sector_id('a-b-c-d-e-f-g-h-987[abcde]'), '987')

        self.assertEqual(_sector_id('not-a-real-room-404[oarel]'), '404')
        self.assertEqual(_sector_id('totally-real-room-200[decoy]'), '200')

    def test_convert_encrypted_name_to_characters(self):
        self.assertEqual(_convert_encrypted_name_to_characters('aaaaa-bbb-z-y-x'), 'abxyz')
        self.assertEqual(_convert_encrypted_name_to_characters('a-b-c-d-e-f-g-h'), 'abcde')

        self.assertEqual(_convert_encrypted_name_to_characters('not-a-real-room'), 'aelor')
        self.assertEqual(_convert_encrypted_name_to_characters('totally-real-room'), 'alort')

        self.assertEqual(_convert_encrypted_name_to_characters('aaffddeeccbb-real-room'), 'abcde')


    def test_is_real_room(self):

        self.assertTrue(is_real_room('not-a-real-room-404[oarel]'))
        self.assertTrue(is_real_room('aaaaa-bbb-z-y-x-123[abxyz]'))
        self.assertTrue(is_real_room('a-b-c-d-e-f-g-h-987[abcde]'))


        self.assertFalse(is_real_room('totally-real-room-200[decoy]'))

    def test_decode_shifted_room(self):
        self.assertEqual(decode_shifted_room('aaaaa-bbb-z-y-x-1[abxyz]'), 'bbbbb-ccc-a-z-y-1[abxyz]')

    def test_shift_encrypted_name(self):

        self.assertEqual(_shift_string('aaaaa-bbb-z-y-x', 1), 'bbbbb-ccc-a-z-y')

