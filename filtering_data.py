from functools import reduce
import re


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # -- usando list comprehensions
    all_python_devs = [worker["name"]
                       for worker in DATA if worker["language"] == "python"]

    # -- usando funciones de orden superior
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    # -- Mapeando un Diccionario, puede funcionar para mapear JSONs
    # -- Nota: La version de Python compatible es 3.9 o mayor
    old_people = list(map(lambda worker: worker | {
        "old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)


def reto():
    # --Crear las listas all_python_devs y all_platzi_workers usando una combinacion de filter y map
    all_python_devs = list(
        filter(lambda worker: worker["language"] == "python", DATA))

    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    all_platzi_workers = list(
        filter(lambda worker: worker["organization"] == "Platzi", DATA)
    )

    all_platzi_workers = list(
        map(lambda worker: worker["name"], all_platzi_workers)
    )

    all_platzi_workers = list(
        reduce(lambda worker: worker["name"], DATA)
    )

    # -- Crear lista old_people y adults con list comprehensions
    old_people = [worker for worker in DATA if worker["age"] > 10]
    #adults = {worker: worker["age"] > 18 for worker in DATA}
    adults = [worker
              for worker in DATA if worker["age"] > 18]

    for old_person in old_people:
        print('Las personas viejas son: ',
              old_person['name'], ' con ', old_person['age'], ' años.')

    for adult in adults:
        print('Los adultos son: ', adult['name'],
              ' con ', adult['age'], ' años.')

    for worker in all_platzi_workers:
        print(worker)


if __name__ == '__main__':
    reto()
    # run()
