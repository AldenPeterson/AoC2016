def is_real_room(room):
    return _sorted_checksum(_checksum(room)) == encrypted_name_values(room)


def _sorted_checksum(checksum):
    return ''.join(sorted(checksum))


def _checksum(room):
    return room[room.find('[', 0) + 1:room.find('[', 0) + 6]


def _sector_id(room):
    bracket_index = room.find('[', 0)
    sectorid_index = room.rfind('-', 0, bracket_index)
    return room[sectorid_index + 1 : bracket_index]


def encrypted_name_values(room):
    return _convert_encrypted_name_to_characters(_encrypted_name(room))


def _encrypted_name(room):
    bracket_index = room.find('[', 0)
    sectorid_index = room.rfind('-', 0, bracket_index)
    return room[:sectorid_index]


def _convert_encrypted_name_to_characters(encrypted_name):
    chars = encrypted_name.replace('-', '')
    d = {}
    for c in chars:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    sorted_values = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))

    s = [c[0] for c in sorted_values[0:5]]

    return ''.join(sorted(s))


def decode_shifted_room(room):
    orig_encrypted_name = _encrypted_name(room)
    sector_id = int(_sector_id(room))
    checksum = _checksum(room)

    return '{encryptedname}-{sectorid}[{checksum}]'.format(
        encryptedname=_shift_string(orig_encrypted_name, sector_id),
        sectorid=sector_id,
        checksum=_shift_string(checksum, sector_id))

def _shift_string(encrypted_name, sector_id):

    # ord(a) = 97
    ascii_a_offset = 97

    new_encrypted_name = ''
    for c in encrypted_name:
        if c != '-':
            cur_ascii = int(ord(c) - ascii_a_offset)
            new_ascii = (cur_ascii + sector_id % 26) % 26 + ascii_a_offset

            c = chr(new_ascii)

        new_encrypted_name += c
    return new_encrypted_name

def main():
    with open('part01.txt') as f:
        input_data = f.read().splitlines()

    sum = 0
    for room in input_data:
        if is_real_room(room):
            sum += int(_sector_id(room))

    print('Part1:', sum)

    # Part two
    for room in input_data:
        new_room = decode_shifted_room(room)
        if new_room.find('north') > -1:
            print('Part2 room:', new_room, ' sectorid:', _sector_id(new_room))
            break



if __name__ == '__main__':
    main()