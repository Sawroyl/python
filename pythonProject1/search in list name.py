students = [
    {"student_id": 1, "name": "Jean Castro", "class": "V"},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]
key = 'name'
value = 'Jean Castro'
if any(i.get(key) == value for i in students):
    print('Key:', {key}, 'and Value:', {value}, 'does exist')
else:
        print('Key:', {key}, 'and Value:', {value}, 'does not exist')
key = 'address'
value = 'New York'
if any(i.get(key) == value for i in students):
    print('Key:', {key}, 'and Value:', {value}, 'does exist')
else:
        print('Key:', {key}, 'and Value:', {value}, 'does not exist')

