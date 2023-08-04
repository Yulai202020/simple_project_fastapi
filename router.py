import os
from fastapi import APIRouter

persons = {
    "0": [
        {"name": "Yulai"},
        {"surname": "Nigmatullin"}
    ],
    "1": [
        {"name": "Azamat"},
        {"surname": "Nigmatullin"}
    ]
}

# Create api router
router = APIRouter()

# Get all Persons
@router.get("/")
async def home_all():
    return persons

# Get person by ID
@router.get("/persons/{person_id}")
async def get_person(person_id: int):
    _person = str(person_id)
    return persons[_person]