import sys
import os
path = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(path)
print(sys.path)

from app.utils.pet_list import getAllPets, queryPets


def test_get_pets():
    pets = getAllPets()
    assert pets is not None and len(pets) != 0


def test_pets_contains_dog():
    pets = queryPets("dog")
    assert pets is not None and len(pets) != 0


def test_pets_not_contains_food():
    pets = queryPets("beaf")
    assert pets is not None and len(pets) == 0
