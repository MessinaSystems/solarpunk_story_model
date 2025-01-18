import json

characters = {}
locations = {}
technology = {}

with open("character.json","r") as file:
    characters = json.load(file)

with open("locations.json","r") as file:
    locations = json.load(file)

with open("technology.json","r") as file:
    technology = json.load(file)


#"city": "highly dense population"
#"me": "A person who enjoys things"
