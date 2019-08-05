"""
practice for loops
keyword: for
"""
#iterate over a list
cities = ["London","New York","Madrid","Paris","Odgen"]
for city in cities:
    print(city)


# iterate over a dictionary
d = {'alice':'801-555-4452154',
     'pedro':'985-658-55874',
     'john':'9985-5587-885478'}

for item in d:
    print(item, "=>", d[item])