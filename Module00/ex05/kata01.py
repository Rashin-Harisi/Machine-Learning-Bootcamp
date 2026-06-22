#!/usr/bin/env python3

#Dictionary key-value pair
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}


for key,value in kata.items():
    print(f"{key} was created by {value}")