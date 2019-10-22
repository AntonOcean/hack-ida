# Все переведено в 10 систему

KEY_PASSWORD = 44334422
KEY_CHAR = 19


def main(username):
    sum = 4546477
    for char in username:
        byte_code = ord(char)
        char_sum = byte_code ^ KEY_CHAR
        sum += char_sum + 1

    password = sum ^ KEY_PASSWORD
    print(password)


if __name__ == '__main__':
    main('0123456788')
