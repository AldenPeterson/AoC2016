import hashlib
from datetime import datetime


class Checker():

    def _hex_hash_from_inputs(self, base, index):
        md5 = hashlib.md5()
        s = base + str(index)
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()

    def hex_hash_matches(self, hex_hash):
        if '00000' == hex_hash[0:5]:
            return True
        return False

    def door_char_from_match(self, hex_hash):
        return hex_hash[5]



    def get_door_password_part1(self, base):

        door_password = ''
        i = -1
        for char in range(8):
            looping = True
            while looping:
                i += 1
                h = self._hex_hash_from_inputs(base, i)
                if self.hex_hash_matches(h):
                    door_password = door_password + self.door_char_from_match(h)
                    print ('Current door password:' + door_password + ' for i=' + str(i) + ' and hash=' + h)
                    looping = False

        return door_password

    def _update_door_password(self, door_password, new_val, new_index):
        new_index = int(new_index)
        return door_password[:new_index] + new_val + door_password[new_index + 1:]

    def get_door_password_part2(self, base):


        initial_char = '-'
        door_password = initial_char * 8
        i = -1

        pw_index_index = 5

        looping = True
        while looping:
            i += 1
            h = self._hex_hash_from_inputs(base, i)
            if self.hex_hash_matches(h):
                try:
                    pw_index = int(h[pw_index_index])
                    print('Match found for i=' + str(i) + ' and h=' + h + ' with door_password=' + door_password + ' and pw_index=' + str(pw_index))
                    if door_password[pw_index] == initial_char:
                        door_password = self._update_door_password(door_password, h[pw_index_index + 1], pw_index)
                        print('Current door password:' + door_password + ' for i=' + str(i) + ' and hash=' + h)

                except Exception as e:
                    pass

                if door_password.find(initial_char) == -1 or i == 10000000:
                    return door_password



def main():
    input_s = 'ojvtpuvg'    # My string
    input_s = 'wtnhxymk'
    c = Checker()
    t1 = datetime.now()
    print()
    print(c.get_door_password_part1(input_s))
    t2 = datetime.now()
    delta = t2 - t1
    print ('Part one time:' + str(delta.total_seconds()))

    t1 = datetime.now()
    print(c.get_door_password_part2(input_s))
    t2 = datetime.now()
    delta = t2 - t1
    print ('Part two time:' + str(delta.total_seconds()))




if __name__ == '__main__':
    main()

#
# numb_results = 8
# base_str = 'abc'
# for i in range(numb_results):
#     looping = True
#     cur_index = -1
#     while looping:
#         cur_index += 1
#         s = base_str + str(cur_index)
#         h = hashlib.md5(s).hexdigest()

