# Uses Key - Value
student = {
 'name': 'franklin', 'age': 25, 'courses': ['Maths', 'CompSC', 'Physisc']
 }

# print(student['courses'])

# Access the key value uses the Get Method

# name = student.get('hdhd', 'Key Not Found')
# print(name)

# Adding a new key value
# student['name'] = 'John'

# print(student.get('name'))


# Updating multiple keys using the update Method
# Takes a dictionary as an args
# student.update(
#  {'name': 'Deno', 'age': 35, 'courses': ['Kiswahili', 'Biology']}
# )

# print(student.get('courses'))


# Deleting a key using del
# del student['age']

# print(student)

# Deleting key using pop Method
# popped = student.pop('name')

# print(popped)

# get all keys
# print(student.keys())

# get all keys
# print(student.values())

# get all key-values pair
# print(student.items())

# Traversing the key-value pair
for key, value in student.items():
    print(key, value)
