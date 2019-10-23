# http://www.backerstreet.com/rec/recdload.htm


def main(username):
    var_10 = 0
    var_14 = 0
    var_16 = 250
    var_17 = 17
    var_15 = 0

    for char in username:
        var_18 = ord(char)

        var_10 += var_15 << 2
        var_10 = var_16 ^ var_10 - var_18

        var_14 += (var_15 << 3)
        var_10 = var_17 ^ var_14 - var_18

        var_15 = var_18

    v32 = (var_14 >> 31 ^ var_14) - (var_14 >> 31)
    v36 = (var_10 >> 31 ^ var_10) - (var_10 >> 31)

    password = f"{v36}-{v32}"

    print(f'Username: {username}\nPassword: {password}')


if __name__ == '__main__':
    main('QAqz!230')
