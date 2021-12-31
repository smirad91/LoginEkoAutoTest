import json


def get(keyword, file="../Lib/loginEko/config.json"):
    with open(file, "r") as f:
        data = json.load(f)
    return data[keyword]
