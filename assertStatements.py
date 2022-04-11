def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]


def run():
    print(palindrome(""))


if __name__ == '__main__':
    run()
