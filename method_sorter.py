def sorter(item):
        return item['name']

presenters=[
    {'name': 'Arthur', 'age': 9},
    {'name': 'Nathaniel', 'age': 11}
]

presenters.sort(key=sorter)
print(presenters)