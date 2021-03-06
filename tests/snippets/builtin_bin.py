assert bin(0) == '0b0'
assert bin(1) == '0b1'
assert bin(-1) == '-0b1'
assert bin(2**24) == '0b1' + '0' * 24
assert bin(2**24-1) == '0b' + '1' * 24
assert bin(-(2**24)) == '-0b1' + '0' * 24
assert bin(-(2**24-1)) == '-0b' + '1' * 24

# TODO: uncomment these tests when arbitrarily sized ints are supported
# assert bin(2**65) == '0b1' + '0' * 65
# assert bin(2**65-1) == '0b' + '1' * 65
# assert bin(-(2**65)) == '-0b1' + '0' * 65
# assert bin(-(2**65-1)) == '-0b' + '1' * 65
