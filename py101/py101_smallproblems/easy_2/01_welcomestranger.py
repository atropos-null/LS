def greetings(list, dictionary):
    name = " ".join(list)
    occupation = " ".join(dictionary.values())
    return f"Hello {name}! Nice to have a {occupation} around!"


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)