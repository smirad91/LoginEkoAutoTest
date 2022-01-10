import json


def get(keyword, file="../Lib/loginEko/test_data.json"):
    with open(file, "r") as f:
        data = json.load(f)
    return data[keyword]
