import json
import src.Word as Word

def read_json():
    words = []
    data = open('Dictionary.json', 'r')
    obj = json.load(data)
    for item in obj["words"]:
        words.append(Word.Word( item['word'], 5, item['meaning']))
    return words