def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "David", "lastname": "Escorcia"}

    super_list = [
        {"firstname": "David", "lastname": "Escorcia"},
        {"firstname": "Daniel", "lastname": "Escorcia"},
        {"firstname": "Rosa", "lastname": "Miranda"},
        {"firstname": "Daniela", "lastname": "Peres"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, ],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [2.3, 5.6, 7.7],
    }

    for key, value in super_dict.items():
        print(key, ":", value)

    """for items in super_list:
        print("\n")
        for key, val in items.items():
            print(key, ":", val)
            """
    """for element in super_list:
        print(element.items())"""

    for elemnt in super_list:
        print(elemnt["firstname"], "-", elemnt["lastname"])


"""(Entry Point)--Esto es una funcion de entrada, es decir, que será lo primero a 
ejecutar al invocar al archivo.py"""

if __name__ == '__main__':
    run()
