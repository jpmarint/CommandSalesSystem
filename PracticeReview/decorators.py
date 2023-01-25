PASSWORD = '12345'


def password_require(func):
    def wrapper():
        password = input('Cuál es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print("La constraseña no es correcta.")

    return wrapper

@password_require
def needs_password():
    print('La constrseña es correcta :)')

def upperL(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    return wrapper

@upperL
def say_my_name(name):
    return f'Hello, {name}'

if __name__ == '__main__':
    #needs_password()
    print(say_my_name('Juan'))