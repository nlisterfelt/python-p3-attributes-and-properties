#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='name', job='Admin'):
        if(type(name)==str and len(name)>0 and len(name)<26 and job in APPROVED_JOBS):
            self.name = name.title()
            self.job = job
        elif(type(name)==str and len(name)>0 and len(name)<26):
            self.name = name.title()
            print("Job must be in list of approved jobs.")
        else:
            print("Name must be string between 1 and 25 characters.")