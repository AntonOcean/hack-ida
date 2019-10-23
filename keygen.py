# bytes to char -> chr()
# char to bytes -> ord()
# in 10 system!

KEY_PASSWORD = 44334422
KEY_NUMBER = 19  # var_14
KEY_CHAR = 136  # var_18


# https://stackoverflow.com/questions/9433541/movsx-in-python
def python_movsx(x, b=8):
    m = 1 << (b - 1)
    x = x & ((1 << b) - 1)
    return (x ^ m) - m


def main(username):
    char_sum = 4546477

    for char in username:
        # mov     eax, [ebp+var_8]
        # movzx   eax, byte ptr [eax]
        byte_code = ord(char)  # var_1A

        # cmp     [ebp+var_1A], 6Dh
        # jle     short loc_401551
        if byte_code <= 109:
            # mov     eax, [ebp+var_14]
            # mov     edx, eax
            # movzx   eax, [ebp+var_1A]
            # xor     eax, edx
            # mov     [ebp+var_9], al
            char_xor = byte_code ^ KEY_NUMBER
        else:
            # mov     eax, [ebp+var_18]
            # mov     edx, eax
            # movzx   eax, [ebp+var_1A]
            # xor     eax, edx
            # mov     [ebp+var_9], al
            # jmp     short loc_40155F
            char_xor = byte_code ^ KEY_CHAR
        
        # loc_40155F:
        # movzx   eax, [ebp+var_9]
        # add     eax, 1
        # mov     [ebp+var_9], al
        # movsx   eax, [ebp+var_9]
        # add     [ebp+var_4], eax
        # add     [ebp+var_8], 1
        char_sum += python_movsx(char_xor + 1)

    # mov     eax, [ebp+var_10]
    # xor     [ebp+var_4], eax
    # mov     eax, [ebp+var_4]
    password = char_sum ^ KEY_PASSWORD

    print(f'Username: {username}\nPassword: {password}')


if __name__ == '__main__':
    main('name_anton')

