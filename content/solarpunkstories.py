import json

characters = {}
regions = {}
technology = {}

with open("character.json","r") as file:
    characters = json.load(file)

with open("locations.json","r") as file:
    regions = json.load(file)

with open("technology.json","r") as file:
    technology = json.load(file)
