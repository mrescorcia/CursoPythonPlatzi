def run():
    squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # --- La siguiente es una implementacion del uso de list comprehensions
    # --- para realizar la operacion anterior en solo una linea de codigo
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)


"""Crear, con un list comprehension, una lista de todos los multiplos de 4 que a la vez
tambien son multiplos de 6 y de 9, hasta 5 digitos."""


def reto_list_comprehensions():
    squares2 = [i*4 for i in range(1, 9999) if (i*4) %
                6 == 0 and (i*4) % 9 == 0]
    print(squares2)


"""(Entry Point)--Esto es una funcion de entrada, es decir, que será lo primero a 
ejecutar al invocar al archivo.py"""
if __name__ == '__main__':
    # run()
    reto_list_comprehensions()
    # reto_dict_comprehension()
