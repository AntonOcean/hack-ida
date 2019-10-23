# bytes to char -> chr()
# char to bytes -> ord()
# in 10 system!

KEY_PASSWORD = 42534253  # var_10
KEY_NUMBER = 226  # var_14
KEY_CHAR = 161  # var_18


# https://stackoverflow.com/questions/9433541/movsx-in-python
def python_movsx(x, b=8):
    m = 1 << (b - 1)
    x = x & ((1 << b) - 1)
    return (x ^ m) - m


def main(username):
    char_sum = 33333333  # var_4

    for char in username:
        byte_code = ord(char)

        if byte_code <= 109:
            char_xor = byte_code ^ KEY_NUMBER
        else:
            char_xor = byte_code ^ KEY_CHAR

        char_sum += python_movsx(char_xor + 77)

    password = char_sum ^ KEY_PASSWORD

    print(f'Username: {username}\nPassword: {password}')


if __name__ == '__main__':
    main('QAqaz0-4')
