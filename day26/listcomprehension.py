numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

# code used in console:
"""
name = "Angela"
new_list = [letter for letter in name]
doubled = [n * 2 for n in range(1,5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
short_names
['Alex', 'Beth', 'Dave']
Caps = [name.upper() for name in names if len(name) >= 5]
"""