from random import randint


def security_code(is_active):
    security_key = ''
    if is_active:
        for i in range(0, 4):
            security_key += str(randint(1, 9))
        print(security_key)
        return security_key
    else:
        print("Please, Activate your 3ds before using this feature")

security_code(True)