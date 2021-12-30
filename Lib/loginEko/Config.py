import json


def get(keyword, file="config.json"):
    with open(file) as f:
        data = json.load(f)
    return data[keyword]
