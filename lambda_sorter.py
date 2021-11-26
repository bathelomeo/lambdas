# Sort Alphabetically
presenters=[
    {'name': 'Arthur', 'age': 9},
    {'name': 'Nathaniel', 'age': 11}
]

presenters.sort(key=lambda item: item['name'])
print('--Alphabetically--')
print(presenters)
# Sort by length (Shortest to longest )
presenters.sort(key=lambda item: len (item['name']))
print('-- length --')
print(presenters)