emp = {
    "id": 101,
    "name": "Chandegara Nirav",
    "designation": "Software Engineer",
    "salary": 75000
}

print("Original Dictionary:", emp)

del emp['designation']

print("After Deleting 'designation':", emp)

emp['name'] = "Jane Doe"

print("After Updating 'name':", emp)
