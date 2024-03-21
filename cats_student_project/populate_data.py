import os

import django
django.setup()
from cats.models import Student, cat

def populate():
    
    cats = [
        {'name': 'Alex', 'student': "Croft"},
        {'name': 'Jill', 'student': "Khan"},
        {'name': 'Joe', 'student': 'Khan'},
        {'name': 'Luna', 'student': 'Croft'},
        {'name': 'Mittens', 'student': 'Croft'},
        {'name': 'Muffins', 'student': 'Doe'},
    ]
    
    
    students = [
        {"first name": 'Alyssa', 'last name': 'Croft', 'number of cats': 3},
        {"first name": 'John', 'last name': 'Doe', 'number of cats': 1},
        {"first name": 'Azam', 'last name': 'Khan', 'number of cats': 2},
        
    ]