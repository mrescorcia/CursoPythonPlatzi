def run():
    # myDict = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         myDict[i] = i**3
    myDict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(myDict)


"""Crear, con dictionary comprehension, un diccionario cuyas llaves sean
 los 1000 primeros numeros naturales con sus raíces cuadradas como valores."""


def reto_dict_comprehension():
    myDict = {i: i**0.5 for i in range(1, 1001)}
    print(myDict)


if __name__ == '__main__':
    reto_dict_comprehension()
