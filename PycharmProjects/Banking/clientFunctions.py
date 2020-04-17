import securityCode as Security
import clientDataBase as Cdb


def make_payment(price):
    is_active = Cdb.dictionary.get("3ds")  # True or False
    security_key = Security.security_code(is_active)
    if is_active:  # False
        user_key = input("Enter 3ds code: ")
        if security_key == user_key:
            print('You have transfered {}$ to Tural Aliyev'.format(price))


make_payment(500)
