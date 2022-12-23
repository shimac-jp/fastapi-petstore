pets = ["dog", "cat", "chicken", "fish"]


def getAllPets() -> list:
    return pets


def queryPets(keyword: str) -> list:
    return [pet for pet in pets if keyword in pet]
