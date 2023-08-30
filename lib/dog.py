#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='name', breed='Mastiff'):
        if(type(name)==str and len(name)>1 and len(name)<25 and breed in APPROVED_BREEDS):
            self.name = name
            self.breed = breed
        elif(type(name)==str and len(name)>1 and len(name)<25):
            self.name = name
            print("Breed must be in list of approved breeds.")
        elif(breed in APPROVED_BREEDS):
            self.breed = breed
            print("Name must be string between 1 and 25 characters.")
        else:
            print("Name must be string between 1 and 25 characters.")
            print("Breed must be in list of approved breeds.")

