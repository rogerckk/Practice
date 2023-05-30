people = [
    {"name": "Harry", "house": "Miri"},
    {"name": "Ben", "house": "Kuching"},
    {"name": "Ken","house": "Sibu"}
]

def f(person):
    return person["name"]

people.sort(key=lambda person: person["name"])

print(people )