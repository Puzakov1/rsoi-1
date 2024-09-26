import pytest
from src.personInterface import Person

print("got here")


person1 = {
    "name": "Ivanov",
    "address": "Moscow",
    "work": "IBM",
    "age": 32
}

person2 = {
    "name": "Smirnov",
    "address": "Parish",
    "work": "Google",
    "age": 20
}

patch_name = {"name": "Alex"}
patch_address = {"address": "London"}
patch_work = {"work": "Architector"}
patch_age = {"age": 21}


@pytest.mark.parametrize("persons", [person1, person2])
def test_create_get(persons):
    id = Person().create_person(persons)
    assert id is not None
    new_person = Person().get_person(id)
    assert new_person["name"] == persons["name"]


@pytest.mark.parametrize("persons, patch_var", [(person1, patch_name), (person1, patch_address),
                                                (person2, patch_work), (person2, patch_age)])
def test_post_patch(persons, patch_var):
    id = Person().create_person(persons)
    assert id is not None
    code = Person().update_person(patch_var, id)
    assert code == 0


@pytest.mark.parametrize("persons", [person1, person2])
def test_post_delete(persons):
    id = Person().create_person(persons)
    assert id is not None
    del_id = Person().delete_person(id)
    assert del_id == id
    new_res = Person().get_person(id)
    assert new_res is None
